swimming = int(input("Swimming Time - "))
cycling = int(input("Cycling Time - "))
running = int(input("Running Time - "))

quali_time = swimming + cycling + running

if quali_time <= 100:
    print("You've won the Provincial Colours")
elif quali_time <= 105:
    print(" You've won the Provincial Half Colours")
elif quali_time <= 110:
    print("You've won the Provincial Scroll")
else:
    print("No award")
