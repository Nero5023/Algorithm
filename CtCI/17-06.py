# -*- coding:utf-8 -*-

class Rearrange:
    # def findSegment(self, A, n):
    #     # write code here
    #     arr = A
    #     sortedArr = sorted(arr)
    #     startIndex = 0
    #     while startIndex < len(arr):
    #         if arr[startIndex] == sortedArr[startIndex]:
    #             startIndex+=1
    #             continue
    #         else:
    #             break
    #     if (startIndex == len(arr)):
    #         return [0,0]
    #     endIndex = len(arr) - 1
    #     while True:
    #         if arr[endIndex] == sortedArr[endIndex]:
    #             endIndex-=1
    #             continue
    #         else:
    #             break
    #     return [startIndex, endIndex]

    # def findSegment(self, A, n):
    #     arr = A
    #     index = 0
    #     while index < len(arr)-1:
    #         if (arr[index] <= arr[index+1]):
    #             index += 1
    #             continue
    #         else:
    #             break
    #     if index == len(arr) - 1:
    #         return [0,0]
    #     value = arr[index+1]
    #     index = 0
    #     while index < len(arr):
    #         if arr[index] <= value:
    #             index += 1
    #             continue
    #         else:
    #             break
    #     start = index

    #     index = len(arr)-1
    #     while index > 1:
    #         if arr[index-1] <= arr[index]:
    #             index -= 1
    #             continue
    #         else:
    #             break

    #     value = arr[index-1]
    #     for i in range(start, index-1):
    #         if arr[i] > value:
    #             value = arr[i]
    #     index = len(arr) - 1
    #     while index > 0:
    #         if arr[index] >= value:
    #             index -= 1
    #             continue
    #         else:
    #             break
    #     end = index
    #     return [start, end]

    def findSegment(self, A, n):
        arr = A
        endLeft = findEndOfLeft(arr)
        if endLeft == len(arr) - 1:
            return [0,0]
        startRight = findStartOfRight(arr)
        print endLeft
        print startRight
        minIndex = endLeft + 1
        maxIndex = endLeft + 1
        for index in range(endLeft+1, startRight):
            if arr[index] < arr[minIndex]:
                minIndex = index
            if arr[index] > arr[maxIndex]:
                maxIndex = index
        left = findFirstSmaller(arr, minIndex, endLeft)
        right = findFirstLarger(arr, maxIndex, startRight)
        return [left, right]

def findEndOfLeft(arr):
    index = 0
    while index < len(arr)-1:
        if (arr[index] <= arr[index+1]):
            index += 1
            continue
        else:
            return index
    return index

def findStartOfRight(arr):
    index = len(arr)-1
    while index > 1:
        if arr[index-1] <= arr[index]:
            index -= 1
            continue
        else:
            return index
    return 0

def findFirstSmaller(arr, minIndex, start):
    v = arr[minIndex]
    for index in range(start-1, -1, -1):
        if arr[index] <= v:
            return index+1
    return 0

def findFirstLarger(arr, maxIndex, start):
    v = arr[maxIndex]
    for index in range(start, len(arr)):
        if arr[index] >= v:
            return index-1
    return len(arr)-1

if __name__ == '__main__':
    print Rearrange().findSegment([1,2,157627,5386,16620,6619,139364,303029,303030],9)