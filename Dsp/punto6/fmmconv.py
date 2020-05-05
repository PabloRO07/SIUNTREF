def fmm_conv(x, m):
    kernel = np.ones(m)/(m+1)
    salida = np.convolve(x, kernel)
    return salida
