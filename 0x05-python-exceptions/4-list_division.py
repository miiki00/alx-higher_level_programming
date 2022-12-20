#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    count = 0
    result_list = []
    while count < list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
            count += 1
    return (result_list)
