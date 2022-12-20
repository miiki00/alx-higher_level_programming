#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed, j = 0, 0
    while j < x:
        try:
            print("{:d}".format(my_list[j]), end='')
        except IndexError:
            raise
        except Exception:
            continue
        else:
            printed += 1
        finally:
            j += 1
    print('')
    return (printed)
