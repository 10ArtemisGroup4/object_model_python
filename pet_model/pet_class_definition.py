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
    def set_name(self):