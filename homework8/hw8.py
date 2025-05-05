import numpy as np

data = [
    [0.01, 0.01, 0.03],
    [0.03, 0.08, 0.07],
    [0.03, 0.06, 0.06],
    [0.07, 0.07, 0.13],
    [0.12, 0.04, 0.03],
    [0.08, 0.07, 0.01],
]


R = {}
for x in range(6):
    for y in range(3):
        r = 3 * x + 9 * y
        R[r] = R.get(r, 0.0) + data[x][y]

R = {k: v for k, v in sorted(R.items())}
print(R)

profits = [r * p for r, p in R.items()]
