contact={}
while True:
    print("contact management system/n")
    print("1.Add contact")
    print("2.search contact")
    print("3.Update contact")
    print("4.delete contact")
    print("5.diplay contact")
    print("6.Exit")
    choice=int(input("Ener a choice:"))
    if choice==1:
        name=input("enter a name")
        phone=input("Enter ph num")
        contact[name]=phone
        print("contact added Successfully")
    elif choice==2:
        name=input("Enter name")
        if name in contact:
            print("phone:",contact[name])
        else:
            print("contact not found")
    elif choice==3:
        name=input("Enter name")
        if name in contact:
            phone=input("Enter new phone")
            contact[name]=phone
            print("updated successfully")
        else:
            print("contact not found")
    elif choice==4:
        name=input("Enter name")
        if name in contact:
            del contact[name]
            print("Deleted successfully")
        else:
            print("contact not found")
    elif choice==5:
        print("\nCONTACT LIST")
        for name,phone in contact.items():
            print(name,"\t",phone)
    elif choice==6:
        print("Thankyou")
        break
    else:
        print("Invalid choice")
      
           
    
    
    
    
