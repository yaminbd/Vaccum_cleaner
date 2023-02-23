####Name: Md Bin Amin Hossan
####ID: HOS20505803 

print("***Welcome to vaccum cleaner***")
print('------------------------------------')

#This class defined: cleaner have 5 actions: move left, move right, move up, move down, clean..
class Cleaner:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self, environment):
        if self.y > 1:
            self.y -= 1
            self.clean(environment)

    def move_right(self, environment):
        if self.y < len(environment[0]):
            self.y += 1
            self.clean(environment)

    def move_up(self, environment):
        if self.x > 1:
            self.x -= 1
            self.clean(environment)

    def move_down(self, environment):
        if self.x < len(environment):
            self.x += 1
            self.clean(environment)

    def clean(self, environment):
        if environment[self.x-1][self.y-1] == "dirt  ":
            environment[self.x-1][self.y-1] = "clean "
   
    def get_environment_with_cleaner(self, environment):
        new_environment = [row.copy() for row in environment]
        new_environment[self.x-1][self.y-1] += "<"
        return new_environment
    


#Defined a Auto_agent to take an actions:
class AutoAgent:
    def get_action(self, environment, cleaner):
        if environment[cleaner.x-1][cleaner.y-1] == "dirt  ":
            return "clean"
        else:
            if cleaner.x % 2 == 1:
                if cleaner.y < len(environment[0]):
                    return "right"
                else:
                    return "down"
            else: 
                if cleaner.y > 1:
                    return "left"
                else:
                    return "down"
                

#Display the environment at goal state;
def is_goal_state(environment):
    for row in environment:
        if "dirt  " in row:
            return False
    return True
                
#This program is reported an error and ask the user to re-enter. 
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            print("Sorry, invalid value. Enter a positive integer.")

#This program is allowed the user to enter two specifications of this environment:
def get_coordinate_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value == 'q':
                return value
            x, y = map(int, value.split(","))
            if x > 0 and y > 0:
                return x, y
        except ValueError:
            print("Sorry, invalid value. Enter a positive coordinates in the format x,y.")


#Created an enviroment [he location using coordinates];
def create_environment(n):
    environment = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("clean ")
        environment.append(row)
    return environment

#This is created mark_dirt to environment by using loaction a loop:
def mark_dirt(environment, x, y):
    environment[x-1][y-1] = "dirt  "


#Display the environment by table format;
def display_environment(environment):
    n = len(environment)
    
    print("+{}+".format("**" * (n * 3 + n + 1)))
    #This loop for decorate row and colum:
    for row in environment:
        print("| {} |".format(" | ".join(row)))
    
    print("+{}+".format("**" * (n * 3 + n + 1)))
    
#This is input to know the size of the environment:
n = get_integer_input("Enter the size of the environment: ")
environment = create_environment(n)
while True:
    #this is the location of the dirt to stop a program;
    dirt_location = get_coordinate_input("Enter the location of the dirt (or type 'q' to stop): ")
    if dirt_location == "q":
        break
    mark_dirt(environment, dirt_location[0], dirt_location[1])

#Display_an environment:
display_environment(environment)
agent_type = input("Do you want to start cleaning: Press - 's' ")

if agent_type == "s":
    agent = AutoAgent()
else:
    print("Invalid input. Try Again!")
    exit()


#Starting a cleaner point (X|Y);
start_location = get_coordinate_input("Enter the start location of the cleaner: ")
cleaner = Cleaner(start_location[0], start_location[1])

while not is_goal_state(environment):
    display_environment(cleaner.get_environment_with_cleaner(environment))
  
    if isinstance(agent, AutoAgent):
        action = agent.get_action(environment, cleaner)
    else:
        print("Invalid agent type.")
        exit()
    if action == "left":
        cleaner.move_left(environment)
        print("Cleaner moved left.")
    elif action == "right":
        cleaner.move_right(environment)
        print("Cleaner moved right.")
    elif action == "up":
        cleaner.move_up(environment)
        print("Cleaner moved up.")
    elif action == "down":
        cleaner.move_down(environment)
        print("Cleaner moved down.")
        cleaner.move_left(environment)
    elif action == "clean":
        cleaner.clean(environment)
        print("Clean")
        
    else:
        print("Invalid action. Try again.")
    
#all the dirt is cleaned, give a notice that the task is completed.
print("Task is completed!")
display_environment(environment)

