def miniMaxSum(arr):
    sum_arr = 0
    for number in arr:
        sum_arr+=number
    max_sum = sum_arr - min(arr)
    min_sum = sum_arr - max(arr)
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
