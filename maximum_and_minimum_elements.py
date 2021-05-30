
data = int(input())
queries = ([])
while data:
    data -= 1
    data_query = (input()).split()[::]
    if data_query[0] == "1":
        a = data_query[1]
        queries.append(a)
    else:
        if queries:
          if data_query[0] == "2":
            queries.pop()
          elif data_query[0] == "3":
            print(max(queries))
          elif data_query[0] == "4":
              print(min(queries))
queries.reverse()
print(', '.join(queries))

