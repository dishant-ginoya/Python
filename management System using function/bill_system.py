data = {'1': 
            {'bill_no':'1','customer_name':'dishant', 'date':'25', 'product':
                                                                    {'product_1':
                                                                            {'product_name':'qwe','product_qty':'1','product_price':'20'},
                                                                     'product_2': 
                                                                            {'product_name':'asd','product_qty':'3','product_price':'25'},
                                                                     'product_3':
                                                                            {'product_name':'zxc','product_qty':'2','product_price':'10'}}},
        '2': 
            {'bill_no':'2','customer_name':'darshan', 'date':'2', 'product':
                                                                    {'product_1':
                                                                            {'product_name':'abc','product_qty':'5','product_price':'10'},
                                                                     'product_2': 
                                                                            {'product_name':'xyz','product_qty':'1','product_price':'16'},
                                                                     'product_3':
                                                                            {'product_name':'poi','product_qty':'3','product_price':'15'},
                                                                     'product_4':
                                                                            {'product_name':'lkj','product_qty':'4','product_price':'20'}}}}



def add_bill():
    bill_no = str(len(data)+1)
    name = str(input(' Enter Customer Name :- '))
    date = str(input(' Enter Date :- '))
    print()
    pro_name = str(input('  Product Name :- '))
    pro_qty = str(input('  Product Qty :- '))
    pro_price = str(input('  Product Price :- '))
    i = 1
    data[bill_no] = {'bill_no':bill_no,'customer_name':name, 'date':date, 'product':{  }}
    while True:
        pro_cat = str('product_') + str(i)
        print()
        ans = str(input('  More Product add (Y/N) - ')).upper()
        if ans == 'Y':
            print()
            pro_name_1 = str(input('  Product Name :- '))
            pro_qty_1 = str(input('  Product Qty :- '))
            pro_price_1 = str(input('  Product Price :- ')) 
            data[bill_no]['product'][pro_cat] = ({'product_name':pro_name_1,'product_qty':pro_qty_1,'product_price':pro_price_1})
            i += 1
        elif ans == 'N':
            data[bill_no]['product'][pro_cat] = ({'product_name':pro_name,'product_qty':pro_qty,'product_price':pro_price})
            break
        else:
            print("\n  **** Please Enter Valid option **** \n")
    All_bill()


def edit_bill(bill_no):
    if 'bill_no' in data:
        print()
        while True:
            ans = str(input('Whould you like change name (Y/N) - ')).upper()
            if ans == 'Y':
                name = str(input('Edit Name :-'))
                data[bill_no]['customer_name'] = name
                break
            elif ans == 'N':
                break
            else:
                print("\n  **** Please Enter Valid bill_no **** \n")


        while True:
            ans = str(input('Whould you like change date (Y/N) - ')).upper()
            if ans == 'Y':
                date = str(input('Edit Date :-'))
                data[bill_no]['date'] = date
                break
            elif ans == 'N':
                break
            else:
                print("\n  **** Please Enter Valid option **** \n")

        for i in range(1,len(data[bill_no]['product'])+1):
            pro_cat = str('product_') + str(i)
            print()
            while True:
                ans = str(input('  Edit ' + pro_cat + ' (Y/N) - ')).upper()
                if ans == 'Y':
                    while True:
                        ans = str(input('   Whould you like change ' + pro_cat + ' name (Y/N) - ')).upper()
                        if ans == 'Y':
                            pro_name = str(input('    Edit ' + pro_cat + ' name :-'))
                            data[bill_no]['product'][pro_cat]['product_name'] = pro_name
                            break
                        elif ans == 'N':
                            break
                        else:
                            print("\n  **** Please Enter Valid option **** \n")

                    while True:
                        ans = str(input('   Whould you like change ' + pro_cat + ' qty (Y/N) - ')).upper()
                        if ans == 'Y':
                            pro_qty = str(input('    Edit ' + pro_cat + ' qty :-'))
                            data[bill_no]['product'][pro_cat]['product_qty'] = pro_qty
                            break
                        elif ans == 'N':
                            break
                        else:
                            print("\n  **** Please Enter Valid option **** \n")

                    while True:
                        ans = str(input('   Whould you like change Prod' + pro_cat + 'uct price (Y/N) - ')).upper()
                        if ans == 'Y':
                            pro_price = str(input('    Edit ' + pro_cat + ' price :-'))
                            data[bill_no]['product'][pro_cat]['product_price'] = pro_price
                            break
                        elif ans == 'N':
                            break
                        else:
                            print("\n  **** Please Enter Valid option **** \n")
                    break
                elif ans == 'N':
                    break
                else:
                    print("\n  **** Please Enter Valid option **** \n")
    else:
        print("\n  **** Please Enter Valid bill number **** \n")



def view_customer(bill_no):
    if 'bill_no' in data:
        print()
        for title,details in data[bill_no].items():
            if type(data[bill_no][title]) is dict:
                pass
            else:
                print(title.ljust(13,' ').title(), ':', details.title())
        print('total product'.ljust(13,' ').title(), ':', len(data[bill_no][title]),'\n')
    else:
        print("\n  **** Please Enter Valid bill number **** \n")


def print_bill(bill_no):
    if 'bill_no' in data:
        print('''
.*******************************.
|                               |''')
        for title,details in data[bill_no].items():

            if type(data[bill_no][title]) is dict:
                pass
            else:
                print('| ',title.ljust(13,' ').title(), ':', details.title().ljust(12,' '),'|')
        print('''|                               |
| ----------------------------- |
|  Name |  Qty  | Price | Total |
| ----------------------------- |''')
        for product in data[bill_no]:
            sub_total = 0
            for product_cat in data[bill_no][product]:
                if type(data[bill_no][product]) is dict:
                    for detail in data[bill_no][product][product_cat].values():
                        total = int(data[bill_no][product][product_cat]['product_qty'])*int(data[bill_no][product][product_cat]['product_price'])
                        print('| ',detail.ljust(5,' ').title() ,end='')
                    print('|',str(total).ljust(5,' '), '|')
                    sub_total += total
        print('''|                       ------- |
|  Grand Total''',''.ljust(9,' ')+''':''',str(str(sub_total)+str(' ₹')).ljust(5,' '),'''|
|                               |
'''+''.ljust(33,'*'))
    else:
        print("\n  **** Please Enter Valid bill number **** \n")

def delete_bill(bill_no):
    if 'bill_no' in data:
        del data[bill_no]
        All_bill()
    else:
        print("\n  **** Please Enter Valid bill number **** \n")

def All_bill():
    print()
    for customer in data:
        for title,details in data[customer].items():
            if type(data[customer][title]) is dict:
                pass
            else:
                print(title.ljust(13,' ').title(), ':', details.title())
        print()


def Choose(option):
    All_bill()
    if option == '1':
        add_bill()
    elif option == '2':
        bill_no = str(input('Which customer do you want to edit product details :- '))
        edit_bill(bill_no)
    elif option == '3':
        bill_no = str(input('Which customer do you want to profile :- '))
        view_customer(bill_no)
    elif option == '4':
        bill_no = str(input('Which customer do you want to print bill :- '))
        print_bill(bill_no)
    elif option == '5':
        bill_no = str(input('Which customer do you want to delete bill :- '))
        delete_bill(bill_no)
    else:
        print("\n  **** Please Enter Valid option **** \n")
    

while True:    
    print("\n ______ Choose option ______")
    print("""
1). For Add Bill
2). For Edit Bill
3). For View Customer Details 
4). For Print Bill
4). For Print Bill
4). For Print Bill
4). For Print Bill
4). For Print Bill
4). For Print Bill
4). For Print Bill
4). For Print Bill
5). For Delete Bill
6). For Exit
""")

    option = str(input("Enter for Choose :- "))

    if option == '6':
        All_bill()
        print("\n *** Thanks for Visiting *** \n")
        break
    else:
        Choose(option)