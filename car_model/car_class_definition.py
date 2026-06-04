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