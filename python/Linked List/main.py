import obj
l=obj.LinkedList()
a=input("Enter first element of the list: ")
l.append(a)
c="a"
while c!="y":
    print(f"\n1.append\n2.prepend\n3.delete by value\n4.delete end\n5.delete head\n6.Display list\n7.Delete by index")
    a=int(input("Enter Which operation to perform: "))
    if a==1:
        b=input("Enter element: ")
        l.append(b)
    elif a==2:
        b=input("Enter element: ")
        l.prepend(b)
    elif a==3:
        b=input("Enter element: ")
        l.delete_node(b)
    elif a==4:
        l.delete_last()
    elif a==5:
        l.delete_first()
    elif a==6:
        l.display()
    elif a==7:
        b=int(input("Enter Index: "))
        l.delete_at_index(b)
    else:
        continue
    c=input("Do you wish to leave?(y for exit)")
