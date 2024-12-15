number = int(input('Enter Number Would You like to Print :- '))

ascii_value = 96
space = 0
for i in range(number):
    a = 0
    print(str('- '*space).replace(' ','-'), end='')
    for j in range(number+ascii_value,ascii_value+i,-1):
        print(chr(j), end=' '.replace(' ','-'))
        a = j
    for r in range(a+1,ascii_value+number+1):
        print(chr(r), end=' '.replace(' ','-'))
    print(('- '*space).replace(' ','-'))
    space += 1
for j in range(number-1,0,-1):
    a = 0
    space -= 1
    print(('- '*int(space-1)).replace(' ','-'), end='')
    for j in range(number+ascii_value,ascii_value+j-1,-1):
        print(chr(j), end=' '.replace(' ','-'))
        a = j
    for r in range(a+1,ascii_value+number+1):
        print(chr(r), end=' '.replace(' ','-'))
    print(('- '*int(space-1)).replace(' ','-'))



# for i in range(number,0,-1):
#     space = number - i
#     print(str('-'*space + '*'*i+'*'*int(i-1) + '-'*space).replace('','-')[1:number*4-2])
# for a in range(2,number+1):
#     space = number - a
#     print(str('-'*space + '*'*a+'*'*int(a-1) + '-'*space).replace('','-')[1:number*4-2])