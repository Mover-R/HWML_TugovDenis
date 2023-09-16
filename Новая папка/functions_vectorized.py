import numpy as np


def prod_non_zero_diag(x):
    return np.prod(np.diag(x,0)[np.diag(x)!=0])
    pass


def are_multisets_equal(x, y):
    return np.sort(x)==np.sort(y)
    pass


def max_after_zero(x):
    return np.max(x[1:][np.nonzero(x[:-1] == 0)])
    pass


def convert_image(img, coefs):
    return np.dot(img, coefs)
    pass


def run_length_encoding(x):
    dif=np.diff(x)
    #print(dif)
    h=np.array([-1])
    h=np.append(h, np.nonzero(dif))
    h+=1
    #print(h)
    a=x[h]
    h=np.append(h,len(x))
    b=np.diff(h)
    return (a,b)
    pass


def pairwise_distance(x, y):
    a=len(x[0])
    b=len(y[0])
    xes1=np.repeat(x[0], b)
    xes1=np.reshape(xes1, (-1, b))
    #print(xes1)
    xes2=np.repeat(y[0], b)
    xes2=np.reshape(xes2, (-1, a))
    #print(xes2)
    ans1=(xes1-xes2)**2
    #print(ans1)
    
    yes1=np.repeat(x[1], b)
    yes1=np.reshape(yes1, (-1, b))
    #print(yes1)
    yes2=np.repeat(y[1], b)
    yes2=np.reshape(yes2, (-1, a))
    #print(yes2)
    ans2=(yes1-yes2)**2
    #print(ans2)
    
    answ=(ans1+ans2)**0.5
    #print(answ)
    return answ
    pass
