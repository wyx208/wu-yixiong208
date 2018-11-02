from random import*
TIMES = 10000
my_first_choice_n=0
my_change_choice_n=0
for i in range(TIMES):
    a="羊1","羊2","车"
    car_inDoor=choice(a)
    my_guess=choice(a)
    if car_inDoor==my_guess:
        my_first_choice_n+=1
    else:
        my_change_choice_n+=1
print("不改选择:{}".format(my_first_choice_n/TIMES))
print("更改选择:{}".format(my_change_choice_n/TIMES))
