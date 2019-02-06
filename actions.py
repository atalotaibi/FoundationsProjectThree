# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "atallah"
my_age = -1
my_bio = "THE BIG PRESIDENT"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    # your code goes here!
    print ("""Would You Like To: \n 1. Creat a New Club.\n 2. Browse and Join Club.\n 3. View Existing Clubs. \n 4. Desplay Members of a Club. \n 5. Close Application.""")
    choice = input("Enter your choice: ")
    if (choice == "1"):
        create_club()
    elif choice == "2":
        join_clubs()
    elif choice == "3":
        view_clubs()
    elif choice == "4":
        view_club_members()
    else:
        print ("You didn't pick the right option")
        exit
    

def create_club():
    # your code goes here!
    club_name = input("Pick a name for your awesome new club: ")
    club_role = input("What is your club about: ")
    user_club = Club(club_name,club_role)
    # user_club.president = myself
    print("Enter the number of people you would like to recruit: ")
    index = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
    i = 0
    
    for candidate in population:
        print ("[%s] %s" %(index[i], candidate.name))
        for x in index:
            int(x)
        i += 1
    while True:
        user_input = int(input())
        if user_input in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
            user_club.recruit_member(population[user_input-1])
            
        elif user_input == -1:
            user_club.recruit_member(myself)
            user_club.assign_president(myself)
            
    
        elif user_input == 0:
            break
        else:
            print ("please, input an appropriate number of a person")
    print ("Here is your club: ")
    print (user_club.name)
    print (user_club.description)
    print ("Members: ")
    user_club.print_member_list()
    total = 0
    for member in user_club.members:
        total += member.age 
    print ("average age in this club: %s years"%(total/len(user_club.members)))
    clubs.append(user_club)
    options()

    

def view_clubs():
    # your code goes here!
    for club in clubs:
        print ("Name: %s"%(club.name))
        print ("Description: %s"%(club.description))
        print ("Members: %d"%s(len(club.members)))
    

def view_club_members():
    # your code goes here!
    # for club in clubs:
    #     print ("Name: %s"%(club.name))
    #     print ("Description: %s"%(club.description))
    #     print ("Members: %d"%(len(club.members)))
    view_clubs()
    club_name = input("Enter the name of the club whose members you would like to see: ")
    for club in clubs:
        if club.name == club_name:
            club.print_member_list()
            break
    else:
        print ("There is no club with this name!")
    options()

  
    
def join_clubs():
    # your code goes here!
    # for club in clubs:
    #     print ("Name: %s"%(club.name))
    #     print ("Description: %s"%(club.description))
    #     print ("Members: %d"%(len(club.members)))
    view_clubs()
    club_name = input("Enter the name of the club you would like to join: ")
    for club in clubs:
        if club.name.lower() == club_name.lower():
            club.recruit_member(myself)
            print ("%s just joind the %s"%(my_name,club.name))
            break
    else:
        print ("There is no club with this name!")
    options()
    

def application():
    introduction()
    
    # your code goes here!
    

