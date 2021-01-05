formulae = [
    '1',
    'x',
    'x**2 - 1',
    'x**3 - 3*x',
    'x**4 - 6*x**2 + 3',
]

for k, f in enumerate(formulae):
    with open(f'dat/hermite/H_{k}.dat', 'w') as dat:
        print(f"#:f='{f}'", file = dat)
        print('#:x H', file = dat)
        for t in range(-500, 501):
            x = t/100
            print(x, eval(f), file = dat)


