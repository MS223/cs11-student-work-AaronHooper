def max_value(integer):
    print range (1, integer + 1)
max_value(10)

def compare_lists():
    list1 = [4,5,15,11,23,42]
    list2 = [1,8,7,16,7,35]
    for x in list1:
        if x > list2[list1.index(x)]:
            print x
        else:
            print list2[list1.index(x)]
compare_lists()


def swapping_stars():
    height = 6
    width = 3
    for x in range (0, height):
        if x % 2 == 1:
            print "- * " * width
        else:
            print '* - ' * width
swapping_stars()
