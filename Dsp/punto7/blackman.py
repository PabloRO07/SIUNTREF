def blackman(xt, m):
    a0 = 0.42
    a1 = 0.5
    a2 = 0.08
    kernel = np.zeros(m)

    i = np.arange(m - 1)
    kernel = a0 - a1 * np.cos((2 * np.pi * i) / (m - 1)) + a2 * np.cos((4 * np.pi * i) / (m - 1))
    y = np.convolve(xt, kernel)
    return y