def pyramid():
    to_print = 1
    going_down = False
    for i in range(0, 7):
        for o in range(0, to_print):
            print("*", end="")

        print("")
        if to_print == 4:
            going_down = True

            if going_down:
                to_print -= 1
            else:
                to_print += 1
    
def pyramid():
    to_print = 1
    going_down = False
    for i in range (0,7):
        for j in range(0, to_print):
            print("*", end="")
        print ("")
        if to_print == 4:
            going_down = True

            if going_down:
                to_print -= 1
            else:
                to_print += 1
