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

# its the number that i need if i would replace the top, bottom, left, right number to an element
place_element_index = 1 # top, bottom
place_element_index2 = 15 # left, right
place_pick = rand.randint(1, 4) # decides random int to place top, bottom, left or right

# algorythm
for i in range(len(sign_list)):
    for j in range(len(elements)):
        if sign_list[i] == elements[j]:
            if elements[j] == "L":
                print("\nElement:", elements[j], "an Stelle", i)
                next_to_L_elements = ["M", "C", "L"]
                pick_random_L_element = rand.randint(0, 2)
                temp_L = next_to_L_elements[pick_random_L_element]

                if place_pick == 1:
                    sign_list[i+place_element_index] = temp_L
                    break
                elif place_pick == 2:
                    sign_list[i-place_element_index] = temp_L
                    break
                elif place_pick == 3:
                    sign_list[i-place_element_index2] = temp_L
                    break
                else:
                    sign_list[i+place_element_index2] = temp_L
                    break
            
            elif elements[j] == "M":
                print("\nElement:", elements[j], "an Stelle", i)
                next_to_M_elements = "L"
                temp_M = next_to_M_elements

                if place_pick == 1:
                    sign_list[i+place_element_index] = temp_M
                    break
                elif place_pick == 2:
                    sign_list[i-place_element_index] = temp_M
                    break
                elif place_pick == 3:
                    sign_list[i-place_element_index2] = temp_M
                    break
                else:
                    sign_list[i+place_element_index2] = temp_M
                    break
            
            elif elements[j] == "C":
                print("\nElement:", elements[j], "an Stelle", i)
                next_to_C_elements = ["L", "S"]
                pick_random_C_element = rand.randint(0, 1)
                temp_C = next_to_C_elements[pick_random_C_element]

                if place_pick == 1:
                    sign_list[i+place_element_index] = temp_C
                    break
                elif place_pick == 2:
                    sign_list[i-place_element_index] = temp_C
                    break
                elif place_pick == 3:
                    sign_list[i-place_element_index2] = temp_C
                    break
                else:
                    sign_list[i+place_element_index2] = temp_C
                    break
            
            elif elements[j] == "S":
                print("\nElement:", elements[j], "an Stelle", i)
                next_to_S_elements = "S"
                temp_S = next_to_S_elements

                if place_pick == 1:
                    sign_list[i+place_element_index] = temp_S
                    break
                elif place_pick == 2:
                    sign_list[i-place_element_index] = temp_S
                    break
                elif place_pick == 3:
                    sign_list[i-place_element_index2] = temp_S
                    break
                else:
                    sign_list[i+place_element_index2] = temp_S
                    break
            

create_field()