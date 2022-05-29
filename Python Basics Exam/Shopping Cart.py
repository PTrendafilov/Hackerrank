n = int(input())
items = {}
for i in range(n):
    name, price = input().split()
    price = int(price)
    items[name] = price
# print(items)
q = int(input())
cart = []
for i in range(q):
    command = input()
    if command=='total':
        print(sum(cart))
    elif command == 'len':
        print(len(cart))
    else:
        command = command.split()
        cart.append(items[command[1]])