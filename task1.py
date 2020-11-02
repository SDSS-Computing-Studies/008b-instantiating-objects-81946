#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
self = ''
class vet:
    animal = None
    breed = None
    name = None
    owner = None
    birthdate = None

    def __init__(self):
        self.animal = input("Enter an animal: ")
        self.breed = input("Enter the breed: ")
        self.name = input("Enter the name: ")
        self.owner = input("Who is the owner: ")
        self.birthdate = input("Enter the birthdate: ")


    def display(self):
        print(self.name + ' ' + self.animal + "\n" + self.breed + ' '+ "is owned by" +' '+ self.owner + "\n" )



# when more than one animal, when call for not latest... will mess up and go vet()

def main():
    ent = 0
    while ent !=3:
        print("\n")
        print("==============================================")
        print("1: Enter a new pet  2: Retrieve a pet  3: Exit")
        print("==============================================")
        ent = input("")
        print("\n")
        ent= int(ent)
        if ent==1:
            animals.append( vet() )
            

        if ent==2:
            # animals is your list
            named = (input("Enter pet's name: ")).strip()
            x=-2
            for i in animals:
                print(x)
                y=x+1
                if named == i.name:
                    x=y-x
                    print(x)
                    print("\n")
                    print(animals[x].display())
                    print("\n")
                    x=1

                    #vet.display(self)  #Put data to be in display
                
                
                

                else:
                    x= x+1
            
            
            if named != animals: 
                pass
                #print("No pet is under that name")
                #main()



        if ent==3:
            print("Exited")
            

  

animals = []
main()


