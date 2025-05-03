def club():
    print('Welcome to the Golf Club Helper!')
    print('Tell me your situation, and I\'ll recommend a club\n')

    hit_green = input('Did you hit on the green (y/n)? ').lower()
    how_far = int(input('How far is the ball from the hole? '))

    if hit_green == 'y':
        print('I recommend using your Putter')
    else:
        if how_far >= 200:
            print('I recommend using your Driver')
        elif how_far >= 140:
            print('I recommend using your 5-Iron')
        elif how_far >= 100:
            print('I recommend using your 9-Iron')
        else:
            print('I recommend using your Pitching Wedge')


club()