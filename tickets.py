
print("Please enter your name: ")
name = raw_input().capitalize()

def greeting():
    print("Hello {}. Welcome to TicketMaster!".format(name))

greeting()

print("Would you like to buy tickets for an event? [y/n]: ")
response = raw_input().capitalize()

def customer_proceed():
    if response == "Yes":
        print("Which film would you like to watch: ")
    else:
        print("Thank you for visiting Alex Cinemas")

customer_proceed()

films  = [
    "A Star is Born",
    "Bohemian Rhapsody",
    "Widower",
    "Venom",
    "Frozen",
    "Halloween"
]

def show_films():
    for film in films:
            print(film)

show_films()

def customer_choice():
    choice = raw_input("Please enter the film you would like to watch from the choices above: ")
