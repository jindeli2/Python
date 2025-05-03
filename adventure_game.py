import time
import sys
import webbrowser
import random
import colorama
from colorama import Fore, Style

class Game:
    def __init__(self):
        print(Fore.WHITE + '\n\t<< Welcome to the dungeon adventure game! >> \n')
        time.sleep(1)
        self.name = str(input("Enter your character's name: ")).upper()
        self.max_health = 20
        self.current_health = self.max_health
        self.max_attack = 10
        print("<< Current health: " + str(self.current_health) + " >> ")
        print("<< Current max attack: " + str(self.max_attack) + " >> ")
        time.sleep(1)

    def slowPrint(self, string):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.025)
        print("")
        time.sleep(.9)

    def attack(self, monster_name, monster_resistance):
        if random.randrange(1, self.max_attack) > monster_resistance:
            self.slowPrint("You slayed the " + monster_name + "!")
            return False
        else:
            if monster_name == "GOBLIN":
                self.current_health -= random.randrange(1, 3)
            elif monster_name == "TROLL":
                self.current_health -= random.randrange(2, 5)
            elif monster_name == "RYGHANTH":
                self.current_health -= random.randrange(4, 8)
            self.slowPrint(Fore.RED + 'You took damage!' + Style.RESET_ALL)
            if self.current_health <= 0:
                self.slowPrint("You died...")
                self.slowPrint("\n\t<< Game Over >>")
                sys.exit()
            print("<< Current health: " + str(self.current_health) + " >>")
            return True


    def prompt(self, type, str_cond="null", int_cond=0):
        prompt_status = True
        while prompt_status:
            if type == "enter":
                user_inp = input("\n\tType [e] to enter the next room: ")
                if user_inp == "e":
                    prompt_status = False
            elif type == "attack":
                user_inp = input("\n\tType [a] to attack! ")
                if user_inp == "a":
                    prompt_status = self.attack(str_cond, int_cond)
            elif type == "drink":
                user_inp = input("\n\tType [d] to drink the potion! ")
                if user_inp == "d":
                    for i in range(3):
                        self.slowPrint(Fore.BLUE + '...'+ Style.RESET_ALL)
                        print("")
                    self.slowPrint("It was a health potion!")
                    self.slowPrint("Bonus health has been added!")
                    self.current_health += 10
                    print("<< Current health: " + str(self.current_health) + " >>")
                    prompt_status = False

    def levelUp(self):
        self.slowPrint(Fore.CYAN + "\n\tLEVEL UP!" + Style.RESET_ALL)
        self.slowPrint("\tHealth has been boosted and restored!")
        self.slowPrint("\tMax attack has been boosted!\n")
        self.max_health += 7
        self.current_health = self.max_health
        self.max_attack += 5
        print("<< Current health: " + str(self.current_health) + " >>")
        print("<< Current max attack: " + str(self.max_attack) + " >>")

    def endGame(self):
        self.slowPrint("RYGHANTH collapses to the ground.")
        self.slowPrint("He says:")
        self.slowPrint("'Bruh'")
        self.slowPrint("'You can take my gold ...'")
        ### uncomment the next line to force the easter egg ###
        #self.current_health = 1
        if self.current_health == 1:
            self.slowPrint("'But one last thing...'")
            for i in range(3):
                self.slowPrint("...")
            self.slowPrint("'You're computer is cursed! ;)'")
            webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=DeeckPeeck")
        else:
            self.slowPrint("'GG...'")
            print("\n\tVICTORY to " + self.name + "!!")
            print("\n << Current health: " + str(self.current_health) + " >>")
           # print("<< Current max attack: " + str(self.max_attack) + " >> \n")
            print("\n>>Thanks for playing!\n")
            


    def story(self):
        self.slowPrint("\nYou wake up cold and afraid in a dark, wet dungeon...")
        self.slowPrint("You see a pair of " + Fore.GREEN + 'green' + Style.RESET_ALL + " eyes looking at you in the corner of the room...")
        self.slowPrint("You have no choice but to attack!!")
        self.prompt("attack", "GOBLIN", 5)
        self.slowPrint("You take the GOBLIN's sword...")
        self.slowPrint("Its body lies in front of an open door...")
        self.prompt("enter")
        self.slowPrint("You see another GOBLIN and a large, ugly TROLL...")
        self.slowPrint("The GOBLIN lunges at you!")
        self.prompt("attack", "GOBLIN", 6)
        self.levelUp()
        self.slowPrint("The TROLL stumbles toward you with his large CLUB...")
        self.prompt("attack", "TROLL", 8)
        self.slowPrint("In the corner of the room, you see a magical potion...")
        self.prompt("drink")
        self.slowPrint("\nYou hear low, deep moaning coming from the next room...")
        self.slowPrint("You feel chills running down your spine...")
        self.prompt("enter")
        self.slowPrint("Four more TROLLS even bigger than the last turn around and look at you...")
        self.slowPrint("They start walking toward you...")
        self.slowPrint("Attack!!")
        for i in range(4):
            self.prompt("attack", "TROLL", 10)
        self.levelUp()
        self.slowPrint("As the last TROLL falls to his knees, you feel an intense wave of heat blast through a narrow doorway...")
        self.slowPrint("A loud, deep roar echoes throughout the dungeon...")
        self.slowPrint("You raise your sword and enter the doorway...")
        self.prompt("enter")
        self.slowPrint("A long, narrow, rickety staircase trails down towards the abyss of the deep dungeon...")
        self.slowPrint("As you walk down the staircase, the heat grows stronger and stronger...")
        self.slowPrint("You reach a set of large wooden double doors...")
        self.prompt("enter")
        self.slowPrint("You enter a massive chamber, filled with gold...")
        self.slowPrint("Except for one corner...")
        self.slowPrint("It's completely dark...")
        self.slowPrint("Until two " + Fore.RED + 'blood-red' + Style.RESET_ALL + " eyes open...")
        self.slowPrint("It's RYGHANTH! The legendary RED DRAGON!")
        self.prompt("attack", "RYGHANTH", 16)
        self.endGame()


def main():
    myGame = Game()
    myGame.story()

main()