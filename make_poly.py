with open('dat/poly.dat', 'w') as dat:
    print('#:x f g h', file = dat)
    for t in range(1, 501):
        x = t/100
        print(x, x, x**2, x**3, file = dat)

