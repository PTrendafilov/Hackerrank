def plusMinus(arr):
    pos = 0
    neg = 0
    zeroes = 0
    for number in arr:
        if number<0:
            neg+=1
        elif number>0:
            pos+=1
        else:
           zeroes+=1
    all_numbers = neg+zeroes+pos
    print(f"{pos/all_numbers:.6f}")
    print(f"{neg/all_numbers:.6f}")
    print(f"{zeroes/all_numbers:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
