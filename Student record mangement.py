
while True:
    print("1.add\n2.view\n3.exit\n")
    choice=input("enter what you want to do :\n")
    if choice=="1":

        try:
          roll_no=int(input("enter the roll no:"))
        except ValueError:
            print("enter only number")
            continue
        name=input("enter the name: ")
        d={
            "roll no":roll_no,
            "name":name

        }
        with open("studentrecord.txt",'a') as file:
            file.write(str(d)+"\n")
        print("data save sucusfully")

    elif choice=="2":
        with open("studentrecord.txt",'r') as file:
            a=file.read()
            print(a)
    elif choice=="3":
        print("thanku for using")
        break
    else:
        print("invalid choice")



            


        

      