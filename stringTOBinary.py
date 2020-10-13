value = input()
string = []
for i in value.split(' '):
    string.append(i)

asci = []
for i in string:
    asci.extend(ord(j) for j in i)

def asciTobin(numbers):
    value = []
    for n in numbers:
        value.append(bin(n).replace('0b',''))
    return value

f_value = asciTobin(asci)
print('Binary value of string:')
for val in f_value:
    print(str(val)+' ', end='')

