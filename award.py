#------Triathlon Awards------

# - Print statement to help the user on how to enter their time
print("Please use this format to enter your time: mins.seconds e.g 30.23\n")

while True:
    # - Create input variables for qualifying times
    swimming = input("Swimming time - ")
    cycling = input("Cycling time - ")
    running = input("Running time - ")

    # - Convert inputs into floats
    try:
        swimming = float(swimming)
        cycling = float(cycling)
        running = float(running)

    except ValueError:
        print("Invalid input! Please enter numeric values")
        continue

    # - Variable for total of qualifying times
    quali_time = swimming + cycling + running
    # - Printing the award depending on the total of qualifying time
    if quali_time <= 100:
        print("\nYou've won the Provincial Colours")
    elif quali_time <= 105:
        print("\nYou've won the Provincial Half Colours")
    elif quali_time <= 110:
        print("\nYou've won the Provincial Scroll")
    else:
        print("No award")

    # - Allow the user to exit the program
    response = input("\nWould you like to enter another time? (yes/no) - ")
    if response.lower() != "yes":
        break