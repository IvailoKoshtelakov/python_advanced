from collections import deque

water = int(input())
command = input()

q = deque()

while not command == "Start":
    person = command
    q.append(person)
    command = input()
command = input()
while not command == "End":
   com = command.split()[0]

   if com == "refill":
        water_refill = command.split()[1]
        water += int(water_refill)
        command = input()
        continue
   com = int(com)
   if water >= com:
            person_get_water = q.popleft()
            water -= com
            print(f"{person_get_water} got water")
   elif water < com:
       person = q.popleft()
       print(f"{person} must wait")
   command = input()
print(f"{water} liters left")