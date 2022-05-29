import os
def findMedian(arr):
    arr = sorted(arr)
    median_index_element = len(arr)//2
    return arr[median_index_element]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()