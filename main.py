from os import system,path
import re

data = {}
seats_no= [51,51,51,51,51,51]
avail_seats_isb_1= [i for i in range(0,seats_no[0])]
avail_seats_isb_2= [j for j in range(0,seats_no[1])]
avail_seats_mlt_1= [k for k in range(0,seats_no[2])]
avail_seats_mlt_2= [l for l in range(0,seats_no[3])]
avail_seats_lhr_1= [m for m in range(0,seats_no[4])]
avail_seats_lhr_2= [n for n in range(0,seats_no[5])]
khi_isb = [[], []]
khi_mlt = [[], []]
khi_lhr = [[], []]

admin = {
    "admin1":"1234",
    "admin2":"1357",
    "mainadmin":"2468"
}
def receipt():
    print("Welcome To Karachi Airport\n","Name:-",data[email]["Name"],sep ="")
    print("E-mail:-",data[email]["email"])
    print("Flight to:-",data[email]["Flight"])
    print("Time:-",data[email]["Time"])
    print("Seats:-",data[email]["Seat"])
    print("Price:-",data[email]["Price"])
def admins():
    while True:
        print("Enter 1 for see the signed up customers")
        print("Enter 2 for see specific logged in customer and their details")
        print("enter 0 to exit")
        choice = int(input("Enter your choice\n"))
        if choice == 1:
            f = open(path.join(path.dirname(path.abspath(__file__)),'emails'),"r")
            print("odd numbered line is email and its next line is its password")
            print(f.read())
            f.close()
        elif choice == 2:
            search = input("search cutomer email")
            if search in data:
                print(data[search])
            else:
                print("email is not there")
        elif choice == 0:
            break
        else:
            print("wrong choice")
        x = input("press '0' to exit or press anyother key to back")
        if x=='0':
            break

def chief():
    while True:
        print("Enter 1 for see the signed up customers")
        print("Enter 2 for see logged in customers and their details")
        print("Enter 3 for changing plane with different number of seated plane")
        print("Enter 4 for adding account for admin")
        print("Enter 5 for watch reserved seats")
        print("enter 0 to exit")
        choice = int(input("Enter your choice\n"))
        if choice == 1:
            f =open(path.join(path.dirname(path.abspath(__file__)),'emails'),"r")
            print("odd numbered line is email and its next line is its password")
            print(f.read())
            f.close()
        elif choice == 2:
            print("enter 1 for seeing whole data of logged in customers")
            print("enter 2 for seeing data of specific logged in customer")
            choice2 = int(input("what is your choice\n"))
            if choice2 == 1:
                print(data)
            elif choice2 == 2:    
                search = input("search cutomer email")
                if search in data:
                    input(data[search])
                else:
                    print("email is not there")
            else:
                print("wrong choice")
        elif choice == 3:
            print("enter 1 if you want to change seats of flight karachi to islamabad of morning shift")
            print("enter 2 if you want to change seats of flight karachi to islamabad of night shift")
            print("enter 3 if you want to change seats of flight karachi to multan of morning shift")
            print("enter 4 if you want to change seats of flight karachi to multan of night shift")
            print("enter 5 if you want to change seats of flight karachi to lahore of morning shift")
            print("enter 6 if you want to change seats of flight karachi to lahore of night shift")
            choice3 = int(input("enter your choice"))
            seats_number=int(input("how many seats do u want in plane (max 65)"))
            seats_number+=1
            if choice3 == 1 and seats_number<67:
                seats_no[0]=seats_number
            elif choice3 == 2 and seats_number<67:
                seats_no[1]=seats_number
            elif choice3 == 3 and seats_number<67:
                seats_no[2]=seats_number
            elif choice3 == 4 and seats_number<67:
                seats_no[3]=seats_number
            elif choice3 == 5 and seats_number<67:
                seats_no[4]=seats_number
            elif choice3 == 6 and seats_number<66:
                seats_no[5]=seats_number
            else:
                print("wrong choice or seat number")
        elif choice == 4:
            id = input("Enter username")
            password1 = input("Enter password")
            admin.update({id:password1})
        elif choice == 5:
            print("enter 1 if you want to chech reserved seats of flight karachi to islamabad of morning shift")
            print("enter 2 if you want to chech reserved seats of flight karachi to islamabad of night shift")
            print("enter 3 if you want to chech reserved seats of flight karachi to multan of morning shift")
            print("enter 4 if you want to chech reserved seats of flight karachi to multan of night shift")
            print("enter 5 if you want to chech reserved seats of flight karachi to lahore of morning shift")
            print("enter 6 if you want to chech reserved seats of flight karachi to lahore of night shift")
            choice5 = int(input("enter your choice"))
            if choice5 == 1:
                print(khi_isb[0])
            elif choice5 == 2:
                print(khi_isb[1])
            elif choice5 ==3:
                print(khi_mlt[0])
            elif choice5 == 4:
                print(khi_mlt[1])
            elif choice5 == 5:
                print(khi_lhr[0])
            elif choice5 == 6:
                print(khi_lhr[1])
            else:
                print("wrong choice")
        elif choice == 0:
            break
        else:
            print("wrong choice")
        x = input("press '0' to exit or press anyother key to go back")
        if x=='0':
            break

def administration():
        while True:
            username = input("Enter your username: ")
            username = username.casefold()
            if username in admin:
                password = input("Enter Password: ")
                if password == admin[username]:
                    system('cls')
                    print("Welcome",username)
                    if username == "mainadmin":
                        chief()
                    else:
                        admins()
                else:
                    print("Incorrect Password")
            else:
                print("Incorrect username")
            x = input("press '0' to exit or press anyother key to again login")
            if x=='0':
                break


def store():
    data.update({email:{"email":email,"Name":name, "Flight":flight,"Seat":seats,"Price":price,"Time":time,}})
def flights():
    global flight
    flight= input("where do you want to go(Islamabad,Multan,Lahore)\n")
    flight = flight.casefold()
    global time
    global seats
    global price
    time = input("when do you want to go in morning shift or night?\n")
    time = time.casefold()
    seats = []
    if time not in ["morning","night"] or flight not in ["islamabad","multan","lahore"]:
        print("Please enter valid city and time")
        return flights()
    elif flight == "islamabad" and time == "morning":
        while len(khi_isb[0])<seats_no[0]:
            for i in range(1,seats_no[0]):
                if i in range(10):
                    print(avail_seats_isb_1[i],end="  ")
                if i in range(10,seats_no[0]):
                        print(avail_seats_isb_1[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Islamabad is 9,300")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[0]):
                if seat not in khi_isb[0]:
                    khi_isb[0].append(seat)
                    seats.append(seat)
                    avail_seats_isb_1.insert((seat),"R")
                    avail_seats_isb_1.remove(seat)
                    price = (len(seats)*9300)
                    price = "{:,}".format(price)            
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")           
    elif flight == "islamabad" and time == "night":
        while len(khi_isb[1])<seats_no[1]:
            for i in range(1,seats_no[1]):
                if i in range(10):
                    print(avail_seats_isb_2[i],end="  ")
                if i in range(10,seats_no[1]):
                        print(avail_seats_isb_2[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Islamabad is 9,300")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[1]):
                if seat not in khi_isb[1]:
                    khi_isb[1].append(seat)
                    seats.append(seat)
                    avail_seats_isb_2.insert((seat),"R")
                    avail_seats_isb_2.remove(seat)
                    price = len(seats)*9300
                    price = "{:,}".format(price) 
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")
    elif flight == "multan" and time == "morning":
        while len(khi_mlt[0])<seats_no[2]:
            for i in range(1,seats_no[2]):
                if i in range(10):
                    print(avail_seats_mlt_1[i],end="  ")
                if i in range(10,seats_no[2]):
                        print(avail_seats_mlt_1[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Multan is 5,000")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[2]):
                if seat not in khi_mlt[0]:
                    khi_mlt[0].append(seat)
                    seats.append(seat)
                    avail_seats_mlt_1.insert((seat),"R")
                    avail_seats_mlt_1.remove(seat)
                    price = len(seats)*5000
                    price = "{:,}".format(price)
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")
    elif flight == "multan" and time == "night":
        while len(khi_mlt[1])<seats_no[3]:
            for i in range(1,seats_no[3]):
                if i in range(10):
                    print(avail_seats_mlt_2[i],end="  ")
                if i in range(10,seats_no[3]):
                        print(avail_seats_mlt_2[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Multan is 5,000")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[3]):
                if seat not in khi_mlt[1]:
                    khi_mlt[1].append(seat)
                    seats.append(seat)
                    avail_seats_mlt_2.insert((seat),"R")
                    avail_seats_mlt_2.remove(seat)
                    price = len(seats)*5000
                    price = "{:,}".format(price) 
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")
    elif flight == "lahore" and time == "morning":
        while len(khi_lhr[0])<seats_no[4]:
            for i in range(1,seats_no[4]):
                if i in range(10):
                    print(avail_seats_lhr_1[i],end="  ")
                if i in range(10,seats_no[4]):
                        print(avail_seats_lhr_1[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Lahore is 7,000")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[4]):
                if seat not in khi_lhr[0]:
                    khi_lhr[0].append(seat)
                    seats.append(seat)
                    avail_seats_lhr_1.insert((seat),"R")
                    avail_seats_lhr_1.remove(seat)
                    price = len(seats)*7000
                    price = "{:,}".format(price)
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")
    elif flight == "lahore" and time == "night":
        while len(khi_lhr[1])<seats_no[5]:
            for i in range(1,seats_no[5]):
                if i in range(10):
                    print(avail_seats_isb_2[i],end="  ")
                if i in range(10,seats_no[5]):
                        print(avail_seats_isb_2[i],end=" ")
                if i%3 == 0:
                    print("  ", end="")
                if i%9 == 0:
                    print("")
            print("\nPrice of per seat of flight Karachi to Lahore is 7,000")
            seat = int(input("\nenter which seat do u want(press '0' if you are done with booking)\n"))
            if seat in range(1,seats_no[5]):
                if seat not in khi_lhr[1]:
                    khi_lhr[1].append(seat)
                    seats.append(seat)
                    avail_seats_lhr_2.insert((seat),"R")
                    avail_seats_lhr_2.remove(seat)
                    price = len(seats)*7000
                    price = "{:,}".format(price)
                else:
                    print("seat is not available")
            elif seat == 0:
                if len(seats)>0:
                    store()
                    receipt()
                break
            else:
                print("seat is not in range")


def signup():
    system('cls')
    f = open(path.join(path.dirname(path.abspath(__file__)),'emails'))
    email = input("Enter your email: ")
    email = email.casefold().strip()
    read = f.read().splitlines()
    emails=read[1:][::2]
    if email not in read:
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
            password = input("Enter password: ")
            if password.strip() == password:
                if len(password) >= 8:
                    a= open(path.join(path.dirname(path.abspath(__file__)),'emails'), 'a')
                    a.writelines(["\n",email,"\n",password])
                    a.close()
                    print("You are signed up")
                else:
                    print("Length must be >= 8.")
            else:
                print("Try again. Your Password contains whitespaces.")
        else:
            print("email is not correct")
    elif email in read:
        print("email is already present")


def login():
    while True:
        f = open(path.join(path.dirname(path.abspath(__file__)),'emails'))
        global email
        global name
        email = input("Enter Email: ")
        email = email.casefold()
        e = f.read().splitlines()
        emails=e[0:][::2]
        passwords=e[1:][::2]
        if email in emails:
            password = input("Enter Password: ")
            if passwords[emails.index(email)] == password:
                system('cls')
                print("Logged In")
                if email in data:
                    receipt()
                else:
                    name = input("what is your name?\n")
                    flights()
            else:
                print("Incorrect")
        else:
            print("email is not correct")
        x = input("press '0' to exit or press anyother key to again login")
        if x=='0':
            break



while True:
    try:
        print("Welcome to Karachi National Airport")
        print("1. Login\n2. Login as Admin\n3. Signup\n4. Exit")
        start =input("Enter choice: ")
        start = start.casefold()
        if start in ["1", "login"]:
            login()
        elif start in ["2","admin","login as admin"]:
            administration()
        elif start in ["3", "signup"]:
            signup()
        elif start in ["4", "exit"]:
            break
        else:
            print("wrong choice")
        input("press enter to go back")
        system('cls')
    except:
        input("Something went Wrong! Please Try again.") 