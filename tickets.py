
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

cinema  = { "films" : [
    {"title": "A Star is Born", "Age": 15, "genre": ["drama", "romance"]},
    {"title": "Bohemian Rhapsody", "Age": "R", "genre": "drama"},
    {"title": "Widower", "Age": 18, "genre": ["action", "thriller"]},
    {"title": "Venom", "Age": 15, "genre": "action"},
    {"title": "Frozen", "Age": "U", "genre": "children"},
    {"title": "Halloween", "Age": 18, "genre": ["horror", "thriller"]},
] }

def show_films():
    for film in cinema["films"]:
        print(film)

show_films()