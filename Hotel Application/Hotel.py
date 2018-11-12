class Hotel:
    visitors = 0
    rooms = ['single', 'double', 'queen', 'king', 'executive']

    @classmethod
    def display_no_of_visitors(cls):
        if Hotel.visitors > 0:
            return "There are currently {} visitor(s)".format(Hotel.visitors)
        else:
            return "There are no visitors currently at the hotel"

    @classmethod
    def from_string(cls, str):
        first_name, last_name, email = str.split(",")
        return cls(first_name, last_name, email)


    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        if '@' in email:
            self.email = email
        else:
            raise TypeError("You have entered an invalid email address")

        Hotel.visitors += 1

    @property
    def email(self):
        return self.email


    def __repr__(self):
        return "Full Name: {} {}\n Email Address: {}".format(self.first_name, self.last_name, self.email)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(" ")


    def checkout(self):
        Hotel.visitors -= 1
        return "{} {} has checked out".format(self.first_name, self.last_name)


jane = Hotel("jane", "doe", "janedoe@gmail.com")

print(jane.first_name)
print(jane.last_name)
print(jane.display_no_of_visitors())
print(jane.email)




