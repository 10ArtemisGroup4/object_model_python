class Car:
    #constructor
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    #getters
    def get_year_model(self):
        return self.__year_model\

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #setters
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    #methods
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed > 0
            self.__speed -= 5

    