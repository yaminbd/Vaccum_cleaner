####Name: Md Bin Amin Hossan
####ID: HOS20505803 

print("***Welcome to vaccum cleaner***")
print('------------------------------------')

                
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

