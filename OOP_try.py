# # # Examples
# # example_list = ["Dave", "Rob", "Stephen"]
# # example_boolean = True
# # example_string = "hello world"
# # print(type(example_list))
# # print(type(example_boolean))
# # print(type(example_string))
# # # Even a function is an instance of the function class!
# # def this_is_a_function(a, b):
# #     return a * b
# # print(type(this_is_a_function))

# class Student():
#     def __init__(self, age, name, gender, grades):
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.grades = grades

#     def calc_ave(self):
#         av = sum(self.grades)/len(self.grades)
#         print("The average for student "+(self.name)+" is "+str(av))

# kate = Student(12, "kate Jackson", "Female", [78, 82])
# steve = Student(14, "Steven Smith", "Male", [12, 56])

# kate.calc_ave()


class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
# First object, provide instance variables for the constructor method
silver_tooth = Wolf("Silvertooth", 5)
# Print out instance variable 'name'
print(silver_tooth.name)
# Print out class variable 'habitat'
print(silver_tooth.habitat)
# Second object
lone_wolf = Wolf("Lone Wolf", 8)
# Print out instance variable 'name'
print(lone_wolf.name)
# Print out class variable 'classification'
print(lone_wolf.classification)

class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False # Defaults to being awake initially
    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Method to put wolf to sleep (self needs to be passed as argument
    # so that all of the properties are available to the method)
    def bed_time(self):
        self.is_sleeping = True
    # Method to wake up wolf (self needs to be passed as argument so
    # that all of the properties are available to the method)
    def wake_up(self):
        self.is_sleeping = False

class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False # Defaults to being awake initially
# Constructor method with instance variables name and age
def __init__(self, name, age):
    self.name = name
    self.age = age
# Method that returns the sleep state of the wolf
def show_sleep_state(self):
    if self.is_sleeping == False:
        return self.name + " is awake"
    else:
        return self.name + " is sleeping"
    # Initialise a wolf object and print the initial sleep
    # state which is awake
    silver_tooth = Wolf("Silver Tooth", 6)
print(silver_tooth.show_sleep_state())
    # Change sleep state to sleeping using dot notation and then print new state
silver_tooth.is_sleeping = True
print(silver_tooth.show_sleep_state)