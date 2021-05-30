
data = input()
stack = []
for el in range(len(data)):
    ch = data[el]
    if ch == "(":
        stack.append(el)
    elif ch == ")":
        j = stack.pop()
        print(data[j:el+1])
