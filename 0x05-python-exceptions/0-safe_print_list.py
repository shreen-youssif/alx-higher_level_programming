#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try :
        while x is not i:
            print(item ,end='')
            i += 1   
    except IndexError:
        None   
    print()
    return i
