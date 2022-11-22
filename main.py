#importing required packages for the program
import getpass,os,random
#databases as dictionaries
database = {} # for register page
Admin = {'USERNAME':'Admin','PASSWORD':'Password'} #for admin
db1 = {'User1':'user1','Pass1':'pass1'} #for login
#all flag variables
count,f,a,c,r = 0,0,0,0,0
#opening screen 
print("  _______ _        _______           _______         \r\n"
				+ " |__   __(_)      |__   __|         |__   __|        \r\n"
				+ "    | |   _  ___     | | __ _  ___     | | ___   ___ \r\n"
				+ "    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\\r\n"
				+ "    | |  | | (__     | | (_| | (__     | | (_) |  __/\r\n"
				+ "    |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|\r\n"
				+ "                                                     \r\n"
				+ "                                                     ")
ch = int(input("Choose one option below : \n 1. Register and Sign up \n 2. Login\n 3. Admin \n Your Choice : "))
os.system('cls')
#Registering Screen
if ch == 1 :
    name = input("Enter your name : ")
    user = input("Create a new username : ")
    pwd = input("Create a unique password : ")
    database[user] = [name,pwd]
    print("Registered Successfully!")
    os.system('cls')
    exit()
#Login Screen
elif ch == 2:
    username = input("Enter the username : ")
    password = getpass.getpass("Enter the password (won't be visible if in cmd) : ",stream=None) 
    if username == db1['User1']:
        f=1
        if password!=db1['Pass1']:
            while count <= 5:
                if password!=db1['Pass1']:
                    password = getpass.getpass("Enter the password again : ")
                    count+=1
                else:
                    move = True
                    break
            else:
                print("You have exceeded the password count of 5. Try again later")
                move = False
                f =0
        else:
            f+=1
            move = True
    else:
        print('Wrong Username or Password')
        exit()
#Admin Screen
elif ch == 3:
    aduser = input("Enter the admin username: ")
    adpass = getpass.getpass("Enter the admin password : ")
    if aduser == Admin['USERNAME']:
        if adpass == Admin['PASSWORD']:
            print("Logged in successfully")
            os.system('cls')
            a+=1
        else:      
            while c <=5:
                if adpass !=Admin['PASSWORD']:
                    adpass = getpass.getpass('Enter the admin password again : ')
                    c+=1
                else:
                    print("Logged in successfully")
                    os.system('cls')
                    break
                    a+=1
        move = False
else:
    print("Select a Valid Choice!")
    move = False
if f!=0:
    print("Logged in successfully")
    os.system('cls')
    move = True
#If the user enters correct login details
if move == True:
    print('Welcome ',db1['User1'])
    #for the gamemode
    mode = input('Select the mode to play \n 1. SinglePlayer \n 2. Multiplayer \n Your Choice : ') 
    os.system('cls')
    if mode == '1' or mode == 1:
        p1 = db1['User1']
        p2 = ' '
    elif mode == '2' or mode == 2:
        p1 = db1['User1']
        p2 = input("Input player two's name : ")# for second player's name
    else:
        print('Invalid Choice')
        exit()
    square_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # list for values
    number_of_turns = 0
    no_wins = True
    p1_pick, p2_pick = "",""
    x = 0
    if (p1 == ""):
        p1 = "Player 1"
    elif (p2 == ""):
        p2 = "Player 2"
    else:
        pass
    p1_pick = input(p1+' choose X or O : ').upper()# player's choice of X or O
    if(p1_pick == 'X'):
        p2_pick='O'
    elif(p1_pick == 'O'):
        p2_pick = 'X'
    else:
        pass
    def compgen(): # for singleplayer mode, uses the computer's random method to generate boxes (might be bugged)
        x = random.randint(1,9)
        for i in square_values:
            if x in square_values:
                break
            else:
                x=random.randint(0,8)
        return x
    def make_a_move(player, player_pick):
        #prints the board below
        print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
        status = True
        while (status == True):
            choice = input(player + " pick a square(" + player_pick + "): ") # asks for user to input the 
            try:
                int(choice)
                if (1 <= int(choice) <= 9):
                    if (square_values[int(choice)-1] != "X" and square_values[int(choice)-1] !="O"):
                        square_values.remove(choice)
                        square_values.insert(int(choice)-1, player_pick)
                        status = False
                    else:
                        print("Square already taken, select another square.") # if the same value is re-entered
                else:
                    print("Input not an option, choose again.")
            except ValueError:
                print("Input not an option, choose again.")
        os.system('cls')
    status_main=True
    def check_win(value1,value2,value3): #checks for wins after each turn
        global status_main
        global no_wins
        if(square_values[value1]=='X' and square_values[value2]=='X' and square_values[value3] == 'X'):
            status_main = False
            no_wins = False
            if(p1_pick == 'X'):
                print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
                print(p1," Won")
            else:
                if mode == '1' or mode ==1:
                    print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
                    print(p2," Won")
                elif mode == '2' or mode ==2:
                    print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
                    print('Computer won and you lost. BIG L for ',p1)  #lol
        elif(square_values[value1]=='O' and square_values[value2]=='O' and square_values[value3] == 'O'):
            status_main = False
            no_wins = False
            if(p1_pick == 'O'):
                print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
                print(p1+" Won")
            else:
                print("""     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n_____|_____|_____ \n     |     |      \n   {} |  {}  |  {}  \n     |     |      """.format(square_values[0], square_values[1], square_values[2],square_values[3], square_values[4], square_values[5], square_values[6],square_values[7],square_values[8]))
                print(p2+" Won")
        else:
            pass
    def func_1(player,pick):#main function consisting of all the other functions
        global number_of_turns
        global status_main
        if (no_wins == True):
            number_of_turns += 1
            make_a_move(player, pick)#checking for wins in all possible combinations
            check_win(0, 1, 2)
            check_win(3, 4, 5)
            check_win(6, 7, 8)
            check_win(0, 3, 6)
            check_win(1, 4, 7)
            check_win(2, 5, 8)
            check_win(0, 4, 8)
            check_win(2, 4, 6)
        if (number_of_turns == 9 and status_main == True):
            print("It's a tie :(")
            status_main = False
            exit()
    if mode == '1' or mode == 1:# Main part of the program which gives input for the main function
        while (status_main == True):
            func_1(p1, p1_pick)
            c = compgen()
            square_values[c]=p2_pick
    elif mode == '2' or mode == 2:
        while (status_main == True):
            func_1(p1, p1_pick)
            func_1(p2,p2_pick)
    else:
        exit()
