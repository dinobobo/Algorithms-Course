def karatsuba_multi(x, y):
    if len(str(x)) < 2 or len(str(y)) < 2:
        return x*y
    else:
        x_l, x_r = divmod(x, 10**(int(len(str(x))/2)))
        y_l, y_r = divmod(y, 10**(int(len(str(y))/2)))
        p0 = karatsuba_multi(x_l, y_l)
        p1 = karatsuba_multi(x_r, y_r)
        p2 = karatsuba_multi((x_l + x_r),(y_l + y_r)) - p0 - p1
        return(p0*10**(2*int(len(str(x))/2)) + p2*10**(int(len(str(x))/2)) + p1)
        
       
    