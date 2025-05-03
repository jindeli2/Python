days = int(input("How many days of scores? "))
total = 0
for i in range(1, days + 1):
    total += int(input("Enter score for day {}: ".format(i)))
print("The total score of the {} days is {}".format(days, total))
