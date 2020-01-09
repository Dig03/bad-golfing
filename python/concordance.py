s=input().split();print({w: (lambda w,ws: s.count(w))(w,s) for w in set(s)})
