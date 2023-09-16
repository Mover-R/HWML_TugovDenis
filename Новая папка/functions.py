def prod_non_zero_diag(x):
    i=len(x)-1
    j=len(x[0])-1     
    s=0
    js=0
    prod=1
    while s<=i and js<=j:
        if (x[s][js]!=0):
            prod*=x[s][js]
        s+=1
        js+=1
    return prod
    pass


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x==y
    pass


def max_after_zero(x):
    max=-100
    for i in range(1,len(x)):
        if x[i-1]==0 and x[i]>max:
            max=x[i]
    return max

    pass


def convert_image(img, coefs):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j]=float(img[i][j][0]) * coefs[0] + float(img[i][j][1]) * coefs[1] + float(img[i][j][2]) * coefs[2]
    return img
    pass


def run_length_encoding(x):
    cnt=0
    p=x[0]
    a=[]
    b=[]
    for i in range(len(x)):
        if p==x[i]:
            cnt++
        else:
            a.append(p)
            b.append(cnt)
            p=x[i]
            cnt=1
    return (a,b)
    pass


def pairwise_distance(x, y):
    ans = []
    for i in range(len(x)):
        ans.append([])
        for j in range(len(y)):
            ans[i].append(((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5)
    return ans
    pass
