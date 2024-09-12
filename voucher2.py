def n():
    p=[int(input(f"P{i+1}?")) for i in range(int(input("NP?")))]
    if int(input("1?(1j,0m)"))==1:j(p)
    while sum(p)>0:
        if sum(m(p))==0: return print("M")
        if sum(j(p))==0: return print("P")
def j(p):
    x=int(input(f"P? {[i+1 for i,v in enumerate(p) if v>0]}:"))-1
    p[x]-=int(input("Pa?"))
    l(p)
    return p
def m(p):
    n=p[0]
    for i in p[1:]:n^=i
    for i,v in enumerate(p):
        if v^n<v:
            p[i]^=n
            break
    else:p[p.index(max(p))]-=1
    l(p)
    return p
def l(p):
    print(f"Pilhas:{p}")
n()