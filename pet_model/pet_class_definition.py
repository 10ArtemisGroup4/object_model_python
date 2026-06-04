class Colors:
    LABEL = "\033[96m"
    VALUE = "\033[97m"
    SUCCESS = "\033[92m"
    ERROR = "\033[91m"
    TITLE = "\033[93m"
    DIM = "\033[90m"
    RESET = "\033[0m"

#pet class
class Pet:

    #constructor
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    #setters
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = name.strip().title()

    def set_animal_type(self, animal_type):
        if not animal_type.strip():
            raise ValueError("Animal type cannot be empty.")
        self.__animal_type = animal_type.strip().title()

    def set_age(self, age):
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age

        #getters
    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age

    #unique feature
def get_fun_fact(self):
    facts = {
        "dog": "Dogs have a sense of smell 40x stronger than humans.",
        "cat": "Cats sleep 12-16 hours a day.",
        "bird": "Some birds can mimic human speech.",
        "fish": "Fish can recognize their owner's face.",
        "rabbit": "Rabbits can jump up to 3 feet high.",
        "hamster": "Hamster can run up to 8 miles a night on their wheel.",
    }
    return facts.get(self.__animal_type.lower(), "Every pet is special in its own way!"
                     )