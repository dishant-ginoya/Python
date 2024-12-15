Account = {'1' : {'User_id':'1','Account_number':'101','Name':'patel dishant','Amount':'1000','Account_type':'saving'},
           '2' : {'User_id':'2','Account_number':'102','Name':'malli darshan','Amount':'2000','Account_type':'saving'},
           '3' : {'User_id':'3','Account_number':'103','Name':'gondaliya himanshu','Amount':'3000','Account_type':'current'}
           }
def add_account():
    print()
    user_id = str(len(Account)+1)
    acc_no = str(len(Account)+100)
    f_name = str(input('Enter your surname :-'))
    l_name = str(input('Enter your name :-'))
    amount = str(input('Enter your Amount :-'))
    acc_type = str(input('Which Account open whould you like ? :- '))
    name = f_name + ' ' + l_name
    Account[user_id] = {'User_id':user_id,'Account_number':acc_no,'Name':name,'Amount':amount,'Account_type':acc_type}
    All_account()


def edit_account(user_id):
    if 'user_id' in Account:
        print()
        ans = str(input('Whould you like change name (Y/N) - ')).upper()
        f_name = str(input('Edit your Surname :-'))
        l_name = str(input('Edit your Name :-'))
        name = f_name + ' ' + l_name
        if ans == 'Y':
            Account[user_id]['Name'] = name

        ans = str(input('Whould you like change Account (Y/N) - ')).upper()
        if ans == 'Y':
            acc_type = str(input('Edit your account type :-'))
            Account[user_id]['Account_type'] = acc_type
        All_account()
    else:
        print("\n  **** Please Enter Valid user_id **** \n")


def view_account(user_id):
    if 'user_id' in Account:
        print()
        for title,details in Account[user_id].items():
            print(title.ljust(15,' '), ':',details.title())
        print()
    else:
        print("\n  **** Please Enter Valid user_id **** \n")
    

def delete_account(user_id):
    if 'user_id' in Account:
        del Account[user_id]
        All_account()
    else:
        print("\n  **** Please Enter Valid user_id **** \n")
    

def transaction(user_id):
    if 'user_id' in Account:
        print()
        ans = str(input(' Whould you like transaction (Y/N) - ')).upper()
        if ans == 'Y':
            print('\n  Deposit for D')
            print('  Withdraw for W','\n')
            transaction = str(input('  Enter (D/W) :- ')).upper()
            if transaction == 'D':
                amount = int(input('  Enter Amount :-'))
                closing_balance = Account[user_id]['Amount']
                total = int(closing_balance) + int(amount)
                Account[user_id]['Amount'] = str(total)

            if transaction == 'W':
                amount = int(input('  Enter Amount :-'))
                closing_balance = Account[user_id]['Amount']
                total = int(closing_balance) - int(amount)
                Account[user_id]['Amount'] = str(total)
        print()
        for title,details in Account[user_id].items():
            print(title.ljust(15,' '), ':',details.title())
        print()
    else:
        print("\n  **** Please Enter Valid user_id **** \n")
    

def All_account():
    print()
    for user_id in Account:
        for title,details in Account[user_id].items():
            print(title.ljust(15,' '), ':',details.title())
        print()


def Choose(option):
    All_account()
    if option == '1':
        add_account()
    elif option == '2':
        user_id = str(input('Which user do you want to edit details :- '))
        edit_account(user_id)
    elif option == '3':
        user_id = str(input('Which user do you want to view profile :- '))
        view_account(user_id)
    elif option == '4':
        user_id = str(input('Which uesr do you want to delete :- '))
        delete_account(user_id)
    elif option == '5':
        user_id = str(input('Which user do you want to transaction :- '))
        transaction(user_id)
    else:
        print("\n  **** Please Enter Valid option **** \n")


while True:    
    print("\n  ______ Choose option ______")
    print("""
1). For Add User
2). For Edit User
3). For Display User
4). For Delete User
5). For Transaction
6). For Exit
""")

    option = str(input("Enter for Choose :- "))

    if option == '6':
        All_account()
        print("\n *** Thanks for Visiting *** \n")
        break
    else:
        Choose(option)