help_button = 'HELP'
start_button = 'START'
stop_button = 'STOP'
quit_button = 'QUIT'
option = ""
second_option = "STOP"
while option.upper() != quit_button:
    option = input(">").upper()
    if option == help_button:
        print('''Start - to start the car
Stop - to stop the car
Quit - to exit''')
    elif option == start_button:
        if option == second_option:
            print('Car is already started')
        else:
            print('Car started...Ready to go')
    elif option == stop_button:
        if option == second_option:
            print('Car is already stopped')
        else:
            print('Car Stopped')
    elif option == quit_button:
        quit()
        break
    else:
        print('I dont understand')
    second_option = option

