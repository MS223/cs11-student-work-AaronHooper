def max_value(integer):
   print range (1,integer + 1)
max_value(51)


def compare_lists():
    list1 = [4,5,15,11,23,42]
    list2 = [1,8,7,16,7,35]
    for x in list1:
        if x > list2[list1.index(x)]:
            print x
        else:
            print list2[list1.index(x)]
compare_lists()
