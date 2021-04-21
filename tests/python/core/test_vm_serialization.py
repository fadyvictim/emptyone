# pylint: disable=invalid-name,protected-access,attribute-defined-outside-init
import pytest
import numpy as np
import mnm
from mnm._core.executor import VMExecutor, Executable, VirtualMachine
from mnm.testing import check, randn, run_infer_type
import tvm
from tvm import relay


def run_exec(exe, inputs):
    vm = VirtualMachine(exe, tvm.cpu())
    out = vm.run(*inputs)
    return out


def serialize_and_load(exe):
    code, lib = exe.save()
    tmp = tvm.contrib.utils.tempdir()
    if lib is not None:
        lib_path = tmp.relpath("lib.so")
        lib.export_library(lib_path)
    code_path = tmp.relpath("code.ro")
    with open(code_path, 'wb') as fo:
        fo.write(code)

    # load from file
    loaded_code = bytearray(open(code_path, 'rb').read())
    loaded_lib = None if lib is None else tvm.runtime.load_module(lib_path)
    return Executable.load_exec(loaded_code, loaded_lib)


@pytest.mark.parametrize("fuse", [True, False])
def test_simple(fuse):
    # pylint: disable=protected-access
    class Model(mnm.Model):
        # pylint: disable=attribute-defined-outside-init
        def build(self):
            pass

        @mnm.model.trace
        def forward(self, x):  # pylint: disable=no-self-use
            y = mnm.add(x, x)
            z = mnm.add(x, y)
            return z

    shape = (3, 3)
    device = 'cpu'
    model = Model()
    model.infer_mode()
    m_x, _ = randn(shape, device=device)
    mod = model._internal(m_x).mod
    if fuse:
        mod = run_infer_type(mod)
        mod = mnm._ffi.pass_.FuseOps(3)(mod)
    executor = VMExecutor(mod, device)
    ref_z = executor.make_executor()(m_x).asnumpy()

    loaded_exe = serialize_and_load(executor.executable)
    m_z = run_exec(loaded_exe, [m_x])
    check(m_z, ref_z)


@pytest.mark.parametrize("fuse", [True, False])
def test_constant(fuse):
    shape = (3, 5)
    konst1 = mnm.ir.const(np.random.randn(1, 5).astype("float32"))
    null = mnm.ir.const(None)
    x = mnm.ir.var("x", shape=shape)
    y = relay.Call(mnm._ffi.op.GetOp("mnm.op.add"), [x, konst1, null, null])
    y = relay.Call(mnm._ffi.op.GetOp("mnm.op.add"), [y, konst1, null, null])
    mod = mnm.ir.IRModule()
    mod["main"] = relay.Function([x], y)
    mod = mnm._ffi.pass_.ToANormalForm()(mod)

    if fuse:
        mod = run_infer_type(mod)
        mod = mnm._ffi.pass_.FuseOps(3)(mod)
    executor = VMExecutor(mod, "cpu")
    m_x, _ = randn(shape)
    ref_y = executor.make_executor()(m_x)

    loaded_exe = serialize_and_load(executor.executable)
    m_y = run_exec(loaded_exe, [m_x])
    check(m_y, ref_y)


@pytest.mark.parametrize("fuse", [True, False])
def test_tuple(fuse):
    rand, _ = randn((1,), device="cpu")
    class Model(mnm.Model):
        def build(self):
            self.c = rand

        @mnm.model.trace
        def forward(self, x):
            pooled = mnm.max_pool2d(x, kernel=(3, 3), stride=1, padding=1)
            return (mnm.add(pooled, self.c), x)
    model = Model()
    m_x, _ = randn((1, 16, 64, 64), device="cpu")
    mod = model._internal(m_x).mod
    if fuse:
        mod = run_infer_type(mod)
        mod = mnm._ffi.pass_.FuseOps(3)(mod)
    executor = VMExecutor(mod, "cpu")
    ref_out = executor.make_executor()(m_x, rand)

    loaded_exe = serialize_and_load(executor.executable)
    out = run_exec(loaded_exe, [m_x, rand])
    assert len(out) == len(ref_out)
    for t, ref_t in zip(out, ref_out):
        check(t, ref_t)


if __name__ == "__main__":
    pytest.main([__file__])
