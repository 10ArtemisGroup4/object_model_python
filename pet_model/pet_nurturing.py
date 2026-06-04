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