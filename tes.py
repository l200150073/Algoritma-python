from random import shuffle as randomi
def swap(a, p, q):
    tmp=a[p]
    a[p]=a[q]
    a[q]=tmp

def cari(a, d, s):
    terk=d
    for i in range(d+1, s):
        if a[i]<a[terk]:
            terk=i
    return terk

def bubble(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                swap(a,j,j+1)

def selection(a):
    n=len(a)
    for i in range(n-1):
        ik=cari(a, i, n)
        if ik !=i:
            swap(a, i, ik)

def insection(a):
    n=len(a)
    for i in range(1, n):
        nilai =a[i]
        pos=i
        while pos>0 and nilai <a[pos-1]:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos]=nilai

k=range(1,50)
randomi(k)
bub=k[:]
sel=k[:]
ins=k[:]
print bub

insection(bub)

print bub
