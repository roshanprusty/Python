largest_num=None
for the_num in [9,24,78,99,66]:
    if largest_num is None:
        largest_num=the_num
    elif the_num>largest_num:
        largest_num=the_num
print("largest value is : ",largest_num)