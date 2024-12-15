list = []

def Is_print():
    print('\nYour new list is =',list,'\n')

def Is_insert(data):
    global list
    [list.insert(imtems[0],int(imtems[1])) for imtems in data.values()]
    Is_print()

def Is_remove(data):
    global list
    list.remove(data)
    Is_print()


def Is_append(data):
    global list
    [list.append(int(value)) for value in data.values() if value != '']
    Is_print()

def Is_sort():
    global list
    list.sort()
    Is_print()

# def Is_pop(data):
def Is_pop():
    global list
    list.pop()
    Is_print()


def Is_reverse():
    global list
    list.reverse()
    Is_print()


def Is_option(choice):
    print()
    if choice == 'p':
        Is_print()


    elif choice == 'i':
        while True:
            try:
                number = int(input(' How times value insert to want you ? :- '))
                data = {}
                for n in range(1,number+1):
                    while True:
                        try:
                            print()
                            index = int(input('  '+str(n)+' Value is which index you want to to insert ? :- '))
                            value = input('  Which Value insert in list ? :- ')
                            data[n] = (index,value)
                            break
                        except ValueError as e:
                            print(' ---- Please Enter Index Number ----\n')
                Is_insert(data)
                break
            except ValueError as e:
                print(' ---- Please Enter Digit ----\n')


    elif choice == 'r':
        while True:
            try:
                value = int(input('  Enter Which value remove you ? :- '))
                if value in list:
                    Is_remove(value)
                    break
                else:
                    print('   Not found value in list\n')
                    continue
            except ValueError as e:
                print(' ---- Please Enter Digit ----\n')


    elif choice == 'a':
        while True:
            try:
                number = int(input(' How Many values append to want you ? :- '))
                data = {}
                for n in range(1,number+1):
                    print()
                    value = input('  Which Value append in list ? :- ')
                    data[n] = value
                Is_append(data)
                break
            except ValueError as e:
                print(' ---- Please Enter Digit ----\n')


    elif choice == 's':
        Is_sort()


    elif choice == 'x':
        Is_pop()
        # while True:
        #     try:
        #         index = int(input(' Which index number value delete to you else last value delete ? :- '))
        #         if not index or len(list) >= index:
        #             Is_pop(index)
        #             break
        #         else:
        #             print('   This index number is out of range \n')
        #     except ValueError as e:
        #         print(' ---- Please Enter Digit ----\n')


    elif choice == 'd':
        Is_reverse()


while True:
        print("""1. P For Print list
2. I For Insert value in list
3. R For Remove value in list
4. A For Append value in list
5. S For Sort in list
6. X For Pop value in list
7. D For Reverse a list
8. Q For Exit
""")
        choice = input('Which Command Perform To You ? :- ').lower()
        if choice in ['p','i','r','a','s','x','d']:
            Is_option(choice)
            continue
        elif choice == 'q':
            break
        print('\n---- Please Enter Valid Option ----\n')
