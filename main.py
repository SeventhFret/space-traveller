from time import sleep

# SPACE TRAVELLER GAME

print('''
You flew on a space shuttle and due to some malfunctions, 
you were forced to land on an unknown planet, which according to scientists is called "HtD-534". 
After a failed landing, your shuttle won't work. Depressurization begins in the case, 
you found many unsoldered cables in the control panel, 
and you need to solder one of the following to the end of the black cable.
''')

soldering_done = False


# LEVEL 1

while soldering_done == False:
    first_choice = input('Which cable will you solder to the black cable?\n[RED/PURPLE/GREEN]\n')
    if first_choice.lower() == 'red':
        for i in 'Soldering...':
                print(i, end='', flush=True)
                sleep(0.15)
        print()
        sleep(0.5)
        print('''BOOM! You choose false cable, a short circuit has occurred and then explosion was happened.
Now you are part of this planet...''')
        print()
        soldering_done = True

    elif first_choice.lower() == 'purple':
        for i in 'Soldering...':
                print(i, end='', flush=True)
                sleep(0.15)
        print()
        sleep(0.5)
        print('''You heard the sound of gears somewhere inside the shuttle... 
It was the right cable, but now you should to solder one more to second black cable to leave that weird planet''')
        second_choise = input('''\nWhich cable will you choose?\n[RED/GREEN]\n''')
        if second_choise.lower() == 'green':
            for i in 'Soldering...':
                print(i, end='', flush=True)
                sleep(0.15)
            print()
            print('God damn yeah! It starts! Now you should to choose the button, which will start the departure...')
            soldering_done = True
        elif second_choise.lower() == 'red':
            for i in 'Soldering...':
                print(i, end='', flush=True)
                sleep(0.15)
            print()
            print('Nothing was happened...')
            soldering_done = True


    elif first_choice.lower() == 'green':
        for i in 'Soldering...':
                print(i, end='', flush=True)
                sleep(0.15)
        print()
        sleep(0.5)
        print('''The shuttle began to vibrate... 
        You heard the countdown and suddenly everything went silent, 
        there is no light in the shuttle anymore and now you are surrounded by darkness....''')
        soldering_done = True



button_pressed = False


# LEVEL 2

while button_pressed == False:
    first_choice = input('Which button will you press to start up your shuttle?\n[YELLOW TRIANGLE/BLUE CIRCLE]\n')
    if first_choice.lower() == 'yellow triangle':
        print('\nPerfekt! Is works!')
        sleep(1)
        print('But now you just turned off your shuttle..\n\n')

    elif first_choice.lower() == 'blue circle':
        print('The shuttle suddenly began to fly away, squeezing you into the chair...')
        print('Congratulations! You leaved this planet!')
        button_pressed = True
      