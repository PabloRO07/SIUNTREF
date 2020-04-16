def conv_circular(xn,hn):
    import numpy as np 
    from matplotlib import pyplot as plt
    xn=np.array(xn)
    hn=np.array(hn)
    l=len(xn)
    print(type(l))
    m=len(hn)
    print(type(m))
    if l!=m:
        zeros1=np.zeros(m-1)
        zeros2=np.zeros(l-1)
        xn=np.hstack((xn,zeros1))
        hn=np.hstack((hn,zeros2))
        print(xn)
        print(hn)
        print(type(xn))
        print(type(hn))
        yn=np.convolve(xn,hn)
    else:
        print(xn)
        print(hn)
        print(type(xn))
        print(type(hn))
        yn=np.convolve(xn,hn)

    print(xn)
    print(hn)
    print(yn)
    return(yn)


conv_circular([1,2,3,1,2,3],[4,5,6,4,5,6])

