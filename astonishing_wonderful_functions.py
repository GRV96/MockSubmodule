def super_ultimate_function(incredible_param):
    return incredible_param + 2


def dull_function(boring_param):
    array = list()

    i = 0
    while i < 10:
        sub_list = list()
        array.append(sub_list)

        j = 0
        while j < 10:
            sub_list.append(super_ultimate_function(i*j*boring_param))
            j += 1

        i += 1

    s = 0
    i = 0
    while i < 10:
        sub_list = array[i]

        j = 0
        while j < 10:
            s += sub_list[j]
            j += 1

        i += 1

    n = 100
    # That's too slow to be funny.
##    n = 0
##    i = 0
##    while True:
##        try:
##            sub_array = array[i]
##        except IndexError:
##            break
##
##        j = 0
##        while True:
##            try:
##                x = sub_array[j]
##                n += 1
##            except IndexError:
##                break

    a = s / n
    return a
