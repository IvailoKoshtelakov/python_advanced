
data = [el[::-1] for el in input().split()]


while data:
   a = data.pop()
   print(''.join(a),end=' ')
