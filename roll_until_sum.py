from random import random
from random import seed

print("This program rolls two 6-sided dice until their sum is a given target value.")
seed(1) 
target = int(input("Enter the target number : ")) 
num_rolls=0;

while(True): 
    num_rolls=num_rolls + 1 
    dice1=(int(random()*10))%6+1 
    dice2=(int(random()*10))%6+1 

    sum = dice1 + dice2 
    print("Roll : ",dice1,"and",dice2, "sum is",sum)
    if(sum == target): 
        break 

print("Got it in",num_rolls,"rolls!")