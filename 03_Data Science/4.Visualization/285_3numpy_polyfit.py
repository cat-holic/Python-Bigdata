import numpy as np

x = np.arange(start=1, stop=15, step=1)
y_linear = x + 5 * np.random.randn(14)
print("x")
print(x)
print("\ny_linear")
print(y_linear)
print("\npolyfit")
print(np.polyfit(x, y_linear, deg=1))

print("\nfn_linear")
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=2))
print(fn_linear)

print(fn_linear(16))

print(fn_linear)
