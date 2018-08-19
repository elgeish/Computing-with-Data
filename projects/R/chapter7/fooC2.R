dyn.load("chapter7/fooC2.so")  # load the compiled C code
a = seq(0, 1, length = 10)
b = seq(0, 1, length = 10)
.Call("fooC2", a, b)
