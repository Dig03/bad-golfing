s=input().split()
print({w: (lambda w,ws: sum([1 if e == w else 0 for e in ws]))(w,s) for w in set(s)})

