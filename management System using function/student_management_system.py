student = {'1' : ['Patel','Dishant','21','MCA'],
           '2' : ['Malli','Darshan','21','BCA'],
           '3' : ['Gondaliya','Himanshu','24','Computer Er.']
           }


def add():
    roll_no = str(len(student)+1)
    f_name = str(input('Enter your surname :-'))
    l_name = str(input('Enter your name :-'))
    age = str(input('Enter your Age :-'))
    Course = str(input('Which Course whould you like join ? :- '))
    student[roll_no] = [f_name, l_name, age, Course]
    All()


def edit(roll_no):
    if 'roll_no' in student:
        print()
        f_ans = str(input('Whould you like change surname (Y/N) ')).upper()
        if f_ans == 'Y':
            f_name = str(input('Edit your Surname :-'))
            student[roll_no][0] = f_name

        l_ans = str(input('Whould you like change name (Y/N) ')).upper()
        if l_ans == 'Y':
            l_name = str(input('Edit your Name :-'))
            student[roll_no][1] = l_name

        a_ans = str(input('Whould you like change age (Y/N) ')).upper()
        if a_ans == 'Y':
            age = str(input('Edit your Age :-'))
            student[roll_no][2] = age

        c_ans = str(input('Whould you like change Course (Y/N) ')).upper()
        if c_ans == 'Y':
            course = str(input('Edit Course :- '))
            student[roll_no][3] = course
        All()
    else:
        print("\n  **** Please Enter Valid roll number **** \n")

def display(roll_no):
    if 'roll_no' in student:
        print("""
Roll No.: """ + roll_no + """
Name    : """ + student[roll_no][0], student[roll_no][1] + """
Age     : """ + student[roll_no][2] + """
Course  : """ + student[roll_no][3])
    else:
        print("\n  **** Please Enter Valid roll number **** \n")  

def delete(roll_no):
    if 'roll_no' in student:
        del student[roll_no]
        All()
    else:
        print("\n  **** Please Enter Valid roll number **** \n")

def All():
    print('\n','Roll no'.ljust(8,' '),'Name'.ljust(20,' '),'Age'.ljust(4,' '),'Course','\n')
    for x in student:
        print(x.center(8,' '), end='  ')
        name = student[x][0] + ' ' + student[x][1]
        print(name.ljust(20,' '), student[x][2].ljust(4,' '), student[x][3])
    print()


def Choose(option):
    All()
    if option == '1':
        add()
    elif option == '2':
        roll_no = str(input('Which student do you want to edit details:-'))
        edit(roll_no)
    elif option == '3':
        roll_no = str(input('Which student do you want to view profile :-'))
        display(roll_no)
    elif option == '4':
        roll_no = str(input('Which student do you want to delete :-'))
        delete(roll_no)
    else:
        print("\n  **** Please Enter Valid option **** \n")


while True:    
    print("\n  ______ Choose option ______")
    print("""
1). For Add student
2). For Edit student
3). For Display student
4). For Delete student
5). For Exit student
""")

    option = str(input("Enter for Choose :- "))

    if option == '5':
        All()
        print("\n *** Thanks for Visiting *** \n")
        break
    else:
        Choose(option)