user_phrase = input('Input your phrase: ')
num_times = int(input('How many times should it be repeated? '))

for number in range(num_times):
    print((number + 1), user_phrase)