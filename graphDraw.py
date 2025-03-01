
def mysqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return x ** 0.5
