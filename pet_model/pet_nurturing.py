from pet_class_definition import Colors, Pet

#color instance
c = Colors()

#title
print(c.TITLE + "\n  ================================" + c.RESET)
print(c.TITLE + "     Pet Information Program    " + c.RESET)
print(c.TITLE + "  ================================\n" + c.RESET)

#input section
print(c.DIM + "Fill in you pet's details below.\n" + c.RESET)

pet = Pet()

while True:
    try:
        pet.set_name(input(c.LABEL + "Enter pet name: " + c.RESET))
        break
    except ValueError as e:
        print(c.ERROR + f"Error: {e}\n" + c.RESET)

while True:
    try:
        pet.set_animal_type(input(c.LABEL + "Enter animal type: " + c.RESET))
        break
    except ValueError as e:
        print(c.ERROR + f"Error: {e}\n" + c.RESET)

while True:
    try:
        pet.set_age(input(c.LABEL + "Enter age(animal years): " + c.RESET))
        break
    except ValueError as e:
        print(c.ERROR + f"Error: {e}\n" + c.RESET)

#output section
print(c.SUCCESS + "\n Pet registered successfully!" + c.RESET)

print(c.TITLE + "\n  --- Pet Information ---" + c.RESET)
print(c.LABEL + "  Name        : " + c.VALUE + pet.get_name()        + c.RESET)
print(c.LABEL + "  Animal Type : " + c.VALUE + pet.get_animal_type() + c.RESET)
print(c.LABEL + "  Age         : " + c.VALUE + str(pet.get_age()) + " year(s)" + c.RESET)
 