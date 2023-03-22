# binary search split set of data in half till target value is found
# assumption - the dataset is sorted already

def binary_search(S, element):
    start = 0
    end = len(S)
    steps = 1

    while start <= end :
        print('Step', steps, ': ', str(S[start :end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == S[middle]:
            return middle
        elif element < S[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


binary_search([1,2,3,4,5,6,7,8],3)