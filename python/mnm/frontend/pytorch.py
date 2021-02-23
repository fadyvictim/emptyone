"""The frontend that converts PyTorch models to Meta models via Relay."""

import torch

from .._core.ndarray import ndarray
from .._lib import relay
from .._ffi.pass_ import FromRelay
from ..frontend.model import FrameworkModel


def from_pytorch(model, shape_dict):
    """Load PyTorch model and convert into Meta via Relay.

    Parameters
    ----------
    model: torch.nn.Module
        The PyTorch module to be converted.

    shape_dict: Dict[str, Tuple[Tuple[int, ...], str]]
        A map from input name to its shape and type. Note that we currently only support
        the model with a single input.

    Returns
    -------
    model: FrameworkModel
        The converted FrameworkModel.
    """
    if len(shape_dict) > 1:
        raise RuntimeError(
            "Do not support PyTorch model with multiple inputs (%d) yet" % len(shape_dict))
    input_name, (input_shape, input_type) = list(shape_dict.items())[0]

    class TraceWrapper(torch.nn.Module):
        """A wrapper to process the forward output. This is required for object detection
        models which have multiple outputs.
        """
        # pylint: disable=missing-function-docstring, abstract-method

        # Enforce the output order of object detection models.
        od_model_output_keys = ["boxes", "scores", "labels", "masks"]

        def __init__(self, model):
            super().__init__()
            self.model = model

        def forward(self, inp):
            out = self.model(inp)
            if isinstance(out, list):
                ordered_outs = [out[0][key] for key in self.od_model_output_keys if key in out[0]]
                return tuple(ordered_outs)
            return out

    model = TraceWrapper(model)
    model.eval()

    if input_type == "float32":
        input_data = torch.randn(input_shape)
    else:
        assert input_type.startswith("int64"), "Unsupported input type %s" % input_type
        input_data = torch.randint(10000, input_shape)

    with torch.no_grad():
        model(input_data)
        scripted_model = torch.jit.trace(model, input_data).eval()
        scripted_model.eval()

    shape_list = [(input_name, input_shape)]
    relay_mod, relay_params = relay.frontend.from_pytorch(scripted_model, shape_list)
    func = FromRelay(relay_mod["main"])
    meta_params = {name: ndarray(data.asnumpy()) for name, data in relay_params.items()}
    return FrameworkModel(func, func, meta_params, {})
