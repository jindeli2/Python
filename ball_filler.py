import math
num = int(input("How many bowling balls will be manufactured? "))
dim = float(input("What is the diameter of each ball in inches? "))
corevol = float(input("What is the core volume in inches cubed? "))
Vol = (4/3)*math.pi*math.pow((dim/2), 3)
requiredVolume = (Vol - corevol)*num
print("You will need", round(requiredVolume, 4),"inches cubed of filter")