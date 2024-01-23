import random as rand

elements = ["L", "S", "C", "M"]
sign = "X"
sign_list = []

for i in range(105):
    sign_list.append(sign)

def create_field():
    # create field
    # there is maybe a better way but for start the project is this enough
    # i will make it better when i have time
    for i in range(105):
        print(sign_list[i], end=" ")
        if i == 14 or i == 29 or i == 44 or i == 59 or i == 74 or i == 89:
            print("")

# create random number
rand_sign_num = rand.randint(0, 105)
rand_element = rand.randint(0, 3)
sign_list[rand_sign_num] = elements[rand_element]
create_field()
