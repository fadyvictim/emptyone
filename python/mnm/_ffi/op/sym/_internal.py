from mnm._lib import _APIS

# pylint: disable=invalid-name,redefined-builtin
# Defined in ./src/op/regs/regs.cc
abs = _APIS.get("mnm.op.sym.abs", None)
# Defined in ./src/op/regs/regs.cc
add = _APIS.get("mnm.op.sym.add", None)
# Defined in ./src/op/regs/regs.cc
avg_pool2d = _APIS.get("mnm.op.sym.avg_pool2d", None)
# Defined in ./src/op/regs/regs.cc
avg_pool2d_dx = _APIS.get("mnm.op.sym.avg_pool2d_dx", None)
# Defined in ./src/op/regs/regs.cc
batch_flatten = _APIS.get("mnm.op.sym.batch_flatten", None)
# Defined in ./src/op/regs/regs.cc
batch_norm_infer = _APIS.get("mnm.op.sym.batch_norm_infer", None)
# Defined in ./src/op/regs/regs.cc
batch_norm_train = _APIS.get("mnm.op.sym.batch_norm_train", None)
# Defined in ./src/op/regs/regs.cc
batch_norm_train_dxwb = _APIS.get("mnm.op.sym.batch_norm_train_dxwb", None)
# Defined in ./src/op/regs/regs.cc
ceil = _APIS.get("mnm.op.sym.ceil", None)
# Defined in ./src/op/regs/regs.cc
collapse_sum_like = _APIS.get("mnm.op.sym.collapse_sum_like", None)
# Defined in ./src/op/regs/regs.cc
conv2d = _APIS.get("mnm.op.sym.conv2d", None)
# Defined in ./src/op/regs/regs.cc
conv2d_dw = _APIS.get("mnm.op.sym.conv2d_dw", None)
# Defined in ./src/op/regs/regs.cc
conv2d_dx = _APIS.get("mnm.op.sym.conv2d_dx", None)
# Defined in ./src/op/regs/regs.cc
copy = _APIS.get("mnm.op.sym.copy", None)
# Defined in ./src/op/regs/regs.cc
cos = _APIS.get("mnm.op.sym.cos", None)
# Defined in ./src/op/regs/regs.cc
divide = _APIS.get("mnm.op.sym.divide", None)
# Defined in ./src/op/regs/regs.cc
equal = _APIS.get("mnm.op.sym.equal", None)
# Defined in ./src/op/regs/regs.cc
erf = _APIS.get("mnm.op.sym.erf", None)
# Defined in ./src/op/regs/regs.cc
erf_dx = _APIS.get("mnm.op.sym.erf_dx", None)
# Defined in ./src/op/regs/regs.cc
floor = _APIS.get("mnm.op.sym.floor", None)
# Defined in ./src/op/regs/regs.cc
get_kept_dims = _APIS.get("mnm.op.sym.get_kept_dims", None)
# Defined in ./src/op/regs/regs.cc
get_reduce_axis = _APIS.get("mnm.op.sym.get_reduce_axis", None)
# Defined in ./src/op/regs/regs.cc
greater = _APIS.get("mnm.op.sym.greater", None)
# Defined in ./src/op/regs/regs.cc
greater_equal = _APIS.get("mnm.op.sym.greater_equal", None)
# Defined in ./src/op/regs/regs.cc
less = _APIS.get("mnm.op.sym.less", None)
# Defined in ./src/op/regs/regs.cc
less_equal = _APIS.get("mnm.op.sym.less_equal", None)
# Defined in ./src/op/regs/regs.cc
log = _APIS.get("mnm.op.sym.log", None)
# Defined in ./src/op/regs/regs.cc
log_softmax = _APIS.get("mnm.op.sym.log_softmax", None)
# Defined in ./src/op/regs/regs.cc
log_softmax_dx = _APIS.get("mnm.op.sym.log_softmax_dx", None)
# Defined in ./src/op/regs/regs.cc
logical_not = _APIS.get("mnm.op.sym.logical_not", None)
# Defined in ./src/op/regs/regs.cc
matmul = _APIS.get("mnm.op.sym.matmul", None)
# Defined in ./src/op/regs/regs.cc
matmul_nt = _APIS.get("mnm.op.sym.matmul_nt", None)
# Defined in ./src/op/regs/regs.cc
matmul_tn = _APIS.get("mnm.op.sym.matmul_tn", None)
# Defined in ./src/op/regs/regs.cc
matmul_tt = _APIS.get("mnm.op.sym.matmul_tt", None)
# Defined in ./src/op/regs/regs.cc
max_pool2d = _APIS.get("mnm.op.sym.max_pool2d", None)
# Defined in ./src/op/regs/regs.cc
max_pool2d_dx = _APIS.get("mnm.op.sym.max_pool2d_dx", None)
# Defined in ./src/op/regs/regs.cc
maximum = _APIS.get("mnm.op.sym.maximum", None)
# Defined in ./src/op/regs/regs.cc
minimum = _APIS.get("mnm.op.sym.minimum", None)
# Defined in ./src/op/regs/regs.cc
mod = _APIS.get("mnm.op.sym.mod", None)
# Defined in ./src/op/regs/regs.cc
multiply = _APIS.get("mnm.op.sym.multiply", None)
# Defined in ./src/op/regs/regs.cc
negative = _APIS.get("mnm.op.sym.negative", None)
# Defined in ./src/op/regs/regs.cc
nll_loss = _APIS.get("mnm.op.sym.nll_loss", None)
# Defined in ./src/op/regs/regs.cc
nll_loss_dpred = _APIS.get("mnm.op.sym.nll_loss_dpred", None)
# Defined in ./src/op/regs/regs.cc
nll_loss_dtrue = _APIS.get("mnm.op.sym.nll_loss_dtrue", None)
# Defined in ./src/op/regs/regs.cc
not_equal = _APIS.get("mnm.op.sym.not_equal", None)
# Defined in ./src/op/regs/regs.cc
relu = _APIS.get("mnm.op.sym.relu", None)
# Defined in ./src/op/regs/regs.cc
relu_dx = _APIS.get("mnm.op.sym.relu_dx", None)
# Defined in ./src/op/regs/regs.cc
reshape = _APIS.get("mnm.op.sym.reshape", None)
# Defined in ./src/op/regs/regs.cc
sgd = _APIS.get("mnm.op.sym.sgd", None)
# Defined in ./src/op/regs/regs.cc
shape = _APIS.get("mnm.op.sym.shape", None)
# Defined in ./src/op/regs/regs.cc
sigmoid = _APIS.get("mnm.op.sym.sigmoid", None)
# Defined in ./src/op/regs/regs.cc
sigmoid_dx = _APIS.get("mnm.op.sym.sigmoid_dx", None)
# Defined in ./src/op/regs/regs.cc
softmax = _APIS.get("mnm.op.sym.softmax", None)
# Defined in ./src/op/regs/regs.cc
softmax_dx = _APIS.get("mnm.op.sym.softmax_dx", None)
# Defined in ./src/op/regs/regs.cc
sqrt = _APIS.get("mnm.op.sym.sqrt", None)
# Defined in ./src/op/regs/regs.cc
sqrt_dx = _APIS.get("mnm.op.sym.sqrt_dx", None)
# Defined in ./src/op/regs/regs.cc
subtract = _APIS.get("mnm.op.sym.subtract", None)
# Defined in ./src/op/regs/regs.cc
sum = _APIS.get("mnm.op.sym.sum", None)
# Defined in ./src/op/regs/regs.cc
tanh = _APIS.get("mnm.op.sym.tanh", None)
# Defined in ./src/op/regs/regs.cc
tanh_dx = _APIS.get("mnm.op.sym.tanh_dx", None)
