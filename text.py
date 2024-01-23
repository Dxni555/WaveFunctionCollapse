elements = ["L", "S", "C", "M"]
sign = "X"
sign_list = []

for i in range(105):
    sign_list.append(sign)

# create field
# there is maybe a better way but for start the project is this enough
# i will make it better when i have time
for i in range(105):
    print(sign_list[i], end=" ")
    if i == 14 or i == 29 or i == 44 or i == 59 or i == 74 or i == 89:
        print("")
