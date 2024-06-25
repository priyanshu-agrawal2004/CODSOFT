list1=[]  
def add():
    name=input("enter your name :-")
    p_no=int(input("enter your phone number :-"))
    email=input("enter your email :-")
    address=input("enter your address :-")
    details={
        "name":name,
        "p_no":p_no,
        "email":email,
        "address":address
    }
    list1.append(details)
def view():
    for i in list1:
        print(i)
        
def delete():
    name=input("enter name to delete in contact")
    for i in list1:
        if(name.lower()==i['name'].lower()):
            list1.remove(i)
            print("contact deleted")
        else:
            print("invalid")
def search():
    name=input("enter name to search in contact")
    for i in list1:
        if(name.lower()==i['name'].lower()):
            print(i)
        else:
            print("contact is not found")
def update():
    name=input("enter name to update contact")
    for i in list1:
        if(name.lower()==i['name'].lower()):
            i['name']=input("enter new name")
            i['p_no']=input("enter new p_no")
            i['email']=input("enter new email")
            i['password']=input("enter new password")
        else:
            print("invalid")
while True:
    print("---: welcome :--")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Update Contact")
    print("6. Exit")

    val =int(input("enter number"))
    if val==1:
        add()
    elif val==2:
        view()
    elif val==3:
        delete()
    elif val==4:
        search()
    elif val==5:
        update()
    else:
        exit()

