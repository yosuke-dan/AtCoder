
short = ['AB','BC','CD','DE','EA','BA','CB','DC','ED','AE']

s = input()
t = input()

if s in short:
    if t in short:
        print('Yes')
    else:
        print('No')
else:
    if t in short:
        print('No')
    else:
        print('Yes')