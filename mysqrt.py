
def mysqrt(x):
    s=1;
    kmax = 10;
    if x <= 0:
        raise ValueError("Cannot compute square root of negative number")

    

    for k in range(kmax):
        s = 0.5 * (s + x / s)
    return s
