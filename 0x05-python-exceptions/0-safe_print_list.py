#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try :
        for item in my_list:
            print(item ,end='')
         i += 1   
    except IndexError:
        None   
    print()
    return i
