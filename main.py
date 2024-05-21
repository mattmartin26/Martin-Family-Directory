
martin_family_branch_members = ['Jim', 'Mike', 'Dick', 'Andy', 'Teresa', 'Dan', 'Cathy', 'Paul', 'Pete', 'Ann-Marie', 'Bob', 'Tom']

class Household:
    """
    The Household class represents a household with a name, address, and members.
    """

    def __init__(self, name, address=''):
        """
        Initialize a new Household instance.

        :param name: Name of the household
        :param address: (Optional) Address of the household
        """
        self.name = name  # Name of the household
        self.address = address  # Address of the household
        self.members = []  # List to store members of the household
        self.num_members = 0  # Number of members in the household

    def update_name(self, new_name):
        self.name = new_name

    def update_address(self, new_address):
        self.address = new_address

    def add_member(self, person):
        self.members.append(person)  # Add the person to the members list
        self.num_members += 1  # Increment the number of members
        person.household = self  # Set the household attribute of the person to this household

    def print_summary(self):
        """
        Print a summary of the household, including its name, address, and members.
        """
        print(f"Household Name: {self.name}\n")  # Print the household name
        print(f"Address: {self.address}\n")  # Print the household address
        print("Members:\n")  # Print the header for the members list
        for member in self.members:  # Iterate through each member in the household
            print(f"{member.fname} {member.lname} ({member.dob})")  # Print the member's details


class Person:
    """
    The Person class represents an individual with personal details and optional household and family branch information.
    """

    def __init__(self, fname, lname, dob, sex, phone, email, household=None, martin_family_branch=None):
        """
        Initialize a new Person instance.

        :param fname: First name of the person
        :param lname: Last name of the person
        :param dob: Date of birth of the person
        :param sex: Sex of the person (M/F)
        :param phone: Phone number of the person
        :param email: Email address of the person
        :param household: (Optional) Household the person belongs to
        :param martin_family_branch: (Optional) Martin family branch the person belongs to
        """
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.sex = sex
        self.phone = phone
        self.email = email
        self.household = household
        self.martin_family_branch = martin_family_branch

    def __str__(self):
        """
        Return a string representation of the Person instance.

        :return: Formatted string with the person's details
        """
        return (f'{self.fname} {self.lname}\n'
                f'Date of Birth: {self.dob}\n'
                f'Sex: {self.sex}\n'
                f'Phone: {self.phone}\n'
                f'Email: {self.email}')


def add_person():
    print("\nLet's add a new person to the family directory!\n")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    sex = input("Sex (M/F): ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    household_name = input("Household Name: ")
    martin_child_name = input(f"Which branch of the Martin family does this person belong to? Enter one of {martin_family_branch_members}: ")

    # Check if the household exists or create a new one
    household = next((h for h in households if h.name == household_name), None)
    if not household:
        household = Household(household_name)
        households.append(household)



    new_person = Person(fname, lname, dob, sex, phone, email)
    print('\n\nCongrats, you have created a new family member:\n')
    print(new_person)


add_person()
