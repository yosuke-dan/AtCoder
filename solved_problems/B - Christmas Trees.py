a, m, l, r = map(int, input().split())

# al = a-l
# alm = al//m
# ra = r-a
# ram = ra//m

## //の仕様を勘違いした

print((a-l)//m + (r-a)//m + 1)