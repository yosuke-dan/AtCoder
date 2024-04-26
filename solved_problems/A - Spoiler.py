# s = input()

# first_bar = s.find('|')
# second_bar = s.find('|',first_bar+1)

# print(s[0:first_bar]+s[second_bar+1:len(s)])


s = input()
first_bar = s.find('|')
second_bar = s.find('|',first_bar+1)
print(s[0:first_bar]+s[second_bar+1:len(s)])