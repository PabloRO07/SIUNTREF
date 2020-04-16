def ejercicio(xn,hn):
    import numpy as np 
    from matplotlib import pyplot as plt 
    
    xn=np.array(xn)
    print(type(xn))
    print(xn)
    hn=np.array(hn)
    print(type(hn))
    print(hn)

    yn=np.convolve(xn,hn)
    print(type(yn))
    print(yn)
    return(yn)

print(ejercicio((1,2,1,1),(1,1,2,1)))