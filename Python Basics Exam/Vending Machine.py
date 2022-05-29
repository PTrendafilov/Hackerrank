num_items, item_price  = input().split()
num_items, item_price = int(num_items), int(item_price)
n = int(input())
for i in range(n):
    req_items, money = input().split()
    req_items, money = int(req_items), int(money)
    if req_items<=num_items:
        if req_items*item_price<=money:
            num_items-=req_items
            print(money-req_items*item_price)
        else:
            print(f'Not enough coins')
    else:
        print(f'Not enough items in the machine')