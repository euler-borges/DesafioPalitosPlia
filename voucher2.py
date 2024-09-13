def n():
    p=[int(input(f"P{i+1}?")) for i in range(int(input("NP?")))]
    if int(input("1?1j,0m")):j(p)
    while sum(p):
        if not sum(m(p)):return print("M")
        if not sum(j(p)):return print("P")
def j(p):
    p[int(input(f"P?{[i+1 for i,v in enumerate(p) if v>0]}:"))-1]-=int(input("Pa?"))
    print(f"{p}");return p
def m(p):
    n=p[0]
    for i in p[1:]:n^=i
    for i,v in enumerate(p):
        if v^n<v:
            p[i]^=n;break
    else:p[p.index(max(p))]-=1
    print(f"{p}");return p
n()