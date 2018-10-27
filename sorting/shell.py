import numpy

def shellSort(numbers):
    
    gap = len(numbers) // 2
    while gap > 0:

        for i in range(gap, len(numbers)):
            temp = numbers[i]
            j = i
# Sort the sub list for this gap
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j = j-gap
            numbers[j] = temp
# Reduce the gap for the next element
        gap = gap//2
    return numbers
