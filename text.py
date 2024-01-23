elements = ["L", "S", "C", "M"]
sign = "X"
sign_list = []

for i in range(100):
    sign_list.append(sign)

for i in range(10):
    for j in range(19):
        print(sign_list[j], end="")
    print(sign_list[i])