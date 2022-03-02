class Dog:
    def __init__(self, the_name, the_age):  # Principal method to call the object
        self.name = the_name
        self.age = the_age

    def say_your_name(self):
        print("I am {}, and I am sitting down here".format(self.name))

    def show_your_age(self):
        print("I am {} years old".format(self.age))

    def say_what_you_like(self):
        print("I like aritmetic")

    def multiply(self, first_operand, second_operand):
        print(f"Easy!, the result is {first_operand * second_operand}")
        # print("The result is ", first_operand * second_operand)

ares = Dog("Ares", 10)
ares.say_your_name()
ares.show_your_age()
ares.say_what_you_like()
ares.multiply(3,5)