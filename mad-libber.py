def main():
    
    print("Madlib Maker") 
    name = input("Enter your name: ") 
    profession = input("What is your profession: ")
    city = input("Please enter a city: ")
    verb = input("Please enter a verb: ")
    friend = input("Please enter another name: ")
    sentenceOne = "\nIt all began with a {1} named {0}."
    sentenceTwo = "Who lived in {2}. "
    sentenceThree = "{0} liked to {3} and throw things at people."
    sentenceFour = "This troubled {0}'s best friend {4}."
    sentenceFive = "The end."
    combinedSentences = [sentenceOne , sentenceTwo , sentenceThree,sentenceFour,sentenceFive]
    for x in combinedSentences:
        print(x.format(name,profession, city,verb,friend))
       
main()