N = input()

if N in ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999','0000']:
    print('Weak')
    exit()

pattern = '1234567890123'

for i in range(10):
    # print(pattern[i:i+4])
    if N == pattern[i:i+4]:
        print('Weak')
        exit()

print('Strong')