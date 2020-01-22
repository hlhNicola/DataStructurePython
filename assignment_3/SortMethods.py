import time
import random

# bubble sort


def bubbleSort(num):
    size = len(num)
    swapped = True
    while swapped is True:
        swapped = False
        for j in range(0, size-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]  # swap them
                swapped = True

# selection sort


def selectionSort(num):
    n = len(num)
    for i in range(0, n):
        min = num[i]
        index = i
        for j in range(i+1, n):
            if num[j] < min:
                min = num[j]
                index = j
                j += 1
        if i != index:
            temp = num[i]
            num[i] = num[index]
            num[index] = temp
        i += 1

# insertion sort


def insertionSort(num):
    n = len(num)
    i = 1
    while i < n:
        item = num[i]
        j = i - 1
        while j >= 0 and num[j] > item:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = item
        i += 1

# -------------------  TEST  -----------------------------------


array = [43, 13, 32, 7, 12, 42, 2, 7]


def testBubbleSort(num):
    bubbleSort(num)
    print('Result of testBubbleSort: ', num)


def testSelectionSort(num):
    selectionSort(num)
    print('Result of selectionSort: ', num)


def testInsertionSort(num):
    insertionSort(num)
    print('Result of selectionSort: ', num)


# testBubbleSort(array)
# testSelectionSort(array)
testInsertionSort(array)

# ------- Get Time Func -----------------------------------------


def getTime(function, input):
    start_time = time.time()
    function(input)
    end_time = time.time()
    return end_time - start_time


# -----------------  Generate Data Sets  -------------------------


def randomSet(num):
    value = random.sample(range(20000), num)
    return value


# ---------  Random Data Sets  -----------------------------------
origin1 = randomSet(2000)
origin2 = randomSet(4000)
origin3 = randomSet(6000)
origin4 = randomSet(8000)
origin5 = randomSet(10000)


randomBubble1 = origin1.copy()
randomBubble2 = origin2.copy()
randomBubble3 = origin3.copy()
randomBubble4 = origin4.copy()
randomBubble5 = origin5.copy()

randomSelect1 = origin1.copy()
randomSelect2 = origin2.copy()
randomSelect3 = origin3.copy()
randomSelect4 = origin4.copy()
randomSelect5 = origin5.copy()

randomInsert1 = origin1.copy()
randomInsert2 = origin2.copy()
randomInsert3 = origin3.copy()
randomInsert4 = origin4.copy()
randomInsert5 = origin5.copy()

timeRandomBubble2000 = getTime(bubbleSort, randomBubble1)
timeRandomBubble4000 = getTime(bubbleSort, randomBubble2)
timeRandomBubble6000 = getTime(bubbleSort, randomBubble3)
timeRandomBubble8000 = getTime(bubbleSort, randomBubble4)
timeRandomBubble10000 = getTime(bubbleSort, randomBubble5)


timeRandomInsert2000 = getTime(insertionSort, randomInsert1)
timeRandomInsert4000 = getTime(insertionSort, randomInsert2)
timeRandomInsert6000 = getTime(insertionSort, randomInsert3)
timeRandomInsert8000 = getTime(insertionSort, randomInsert4)
timeRandomInsert10000 = getTime(insertionSort, randomInsert5)


timeRandomSelect2000 = getTime(selectionSort, randomSelect1)
timeRandomSelect4000 = getTime(selectionSort, randomSelect2)
timeRandomSelect6000 = getTime(selectionSort, randomSelect3)
timeRandomSelect8000 = getTime(selectionSort, randomSelect4)
timeRandomSelect10000 = getTime(selectionSort, randomSelect5)


print('RANDOM: ')
print(timeRandomBubble2000, timeRandomSelect2000, timeRandomInsert2000)
print(timeRandomBubble4000, timeRandomSelect4000, timeRandomInsert4000)
print(timeRandomBubble6000, timeRandomSelect6000, timeRandomInsert6000)
print(timeRandomBubble8000, timeRandomSelect8000, timeRandomInsert8000)
print(timeRandomBubble10000, timeRandomSelect10000, timeRandomInsert10000)


# ---------  Sorted Data Sets  -----------------------------------
origin1.sort()
origin2.sort()
origin3.sort()
origin4.sort()
origin5.sort()


sortedBubble1 = origin1.copy()
sortedBubble2 = origin2.copy()
sortedBubble3 = origin3.copy()
sortedBubble4 = origin4.copy()
sortedBubble5 = origin5.copy()

sortedSelect1 = origin1.copy()
sortedSelect2 = origin2.copy()
sortedSelect3 = origin3.copy()
sortedSelect4 = origin4.copy()
sortedSelect5 = origin5.copy()

sortedInsert1 = origin1.copy()
sortedInsert2 = origin2.copy()
sortedInsert3 = origin3.copy()
sortedInsert4 = origin4.copy()
sortedInsert5 = origin5.copy()


timeSortedBubble2000 = getTime(bubbleSort, sortedBubble1)
timeSortedBubble4000 = getTime(bubbleSort, sortedBubble2)
timeSortedBubble6000 = getTime(bubbleSort, sortedBubble3)
timeSortedBubble8000 = getTime(bubbleSort, sortedBubble4)
timeSortedBubble10000 = getTime(bubbleSort, sortedBubble5)


timeSortedInsert2000 = getTime(insertionSort, sortedInsert1)
timeSortedInsert4000 = getTime(insertionSort, sortedInsert2)
timeSortedInsert6000 = getTime(insertionSort, sortedInsert3)
timeSortedInsert8000 = getTime(insertionSort, sortedInsert4)
timeSortedInsert10000 = getTime(insertionSort, sortedInsert5)


timeSortedSelect2000 = getTime(selectionSort, sortedSelect1)
timeSortedSelect4000 = getTime(selectionSort, sortedSelect2)
timeSortedSelect6000 = getTime(selectionSort, sortedSelect3)
timeSortedSelect8000 = getTime(selectionSort, sortedSelect4)
timeSortedSelect10000 = getTime(selectionSort, sortedSelect5)

print('SORTED: ')
print(timeSortedBubble2000, timeSortedSelect2000, timeSortedInsert2000)
print(timeSortedBubble4000, timeSortedSelect4000, timeSortedInsert4000)
print(timeSortedBubble6000, timeSortedSelect6000, timeSortedInsert6000)
print(timeSortedBubble8000, timeSortedSelect8000, timeSortedInsert8000)
print(timeSortedBubble10000, timeSortedSelect10000, timeSortedInsert10000)


# ---------  Reverse Data Sets  -----------------------------------
origin1.sort(reverse=True)
origin2.sort(reverse=True)
origin3.sort(reverse=True)
origin4.sort(reverse=True)
origin5.sort(reverse=True)


reversedBubble1 = origin1.copy()
reversedBubble2 = origin2.copy()
reversedBubble3 = origin3.copy()
reversedBubble4 = origin4.copy()
reversedBubble5 = origin5.copy()

reversedSelect1 = origin1.copy()
reversedSelect2 = origin2.copy()
reversedSelect3 = origin3.copy()
reversedSelect4 = origin4.copy()
reversedSelect5 = origin5.copy()

reversedInsert1 = origin1.copy()
reversedInsert2 = origin2.copy()
reversedInsert3 = origin3.copy()
reversedInsert4 = origin4.copy()
reversedInsert5 = origin5.copy()


timeReversedBubble2000 = getTime(bubbleSort, reversedBubble1)
timeReversedBubble4000 = getTime(bubbleSort, reversedBubble2)
timeReversedBubble6000 = getTime(bubbleSort, reversedBubble3)
timeReversedBubble8000 = getTime(bubbleSort, reversedBubble4)
timeReversedBubble10000 = getTime(bubbleSort, reversedBubble5)


timeReversedInsert2000 = getTime(insertionSort, reversedInsert1)
timeReversedInsert4000 = getTime(insertionSort, reversedInsert2)
timeReversedInsert6000 = getTime(insertionSort, reversedInsert3)
timeReversedInsert8000 = getTime(insertionSort, reversedInsert4)
timeReversedInsert10000 = getTime(insertionSort, reversedInsert5)


timeReversedSelect2000 = getTime(selectionSort, reversedSelect1)
timeReversedSelect4000 = getTime(selectionSort, reversedSelect2)
timeReversedSelect6000 = getTime(selectionSort, reversedSelect3)
timeReversedSelect8000 = getTime(selectionSort, reversedSelect4)
timeReversedSelect10000 = getTime(selectionSort, reversedSelect5)

print('REVERSED: ')
print(timeReversedBubble2000, timeReversedSelect2000, timeReversedInsert2000)
print(timeReversedBubble4000, timeReversedSelect4000, timeReversedInsert4000)
print(timeReversedBubble6000, timeReversedSelect6000, timeReversedInsert6000)
print(timeReversedBubble8000, timeReversedSelect8000, timeReversedInsert8000)
print(timeReversedBubble10000, timeReversedSelect10000, timeReversedInsert10000)









