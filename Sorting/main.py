import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def swap(y_arr, a, b):
    temp = y_arr[a]
    y_arr[a] = y_arr[b]
    y_arr[b] = temp

def bubblesort(y_arr):
    for i in range(len(y_arr)-1, -1, -1):
        for j in range(0, i):
            if y_arr[j] > y_arr[j+1]:
                swap(y_arr, j, j+1)
                yield y_arr

def insertionsort(y_arr):
    for i in range(1,len(y_arr)):
        for j in range(i, 0, -1):
            if y_arr[j] < y_arr[j-1]:
                swap(y_arr, j, j-1)
                yield y_arr
            else:
                break

def selectionsort(y_arr):
    for i in range(len(y_arr)-1, 0, -1):
        highest = 0
        for j in range(0, i):
            if y_arr[highest] < y_arr[j]:
                highest = j
        if y_arr[highest] > y_arr[i]:
            swap(y_arr, highest, i)
            yield y_arr

def merge(y_arr, start, middle, end):
    start2 = middle + 1
    if y_arr[middle] <= y_arr[middle+1]:
        yield y_arr
        return
    while start < start2 and start2 <= end:
        if y_arr[start] < y_arr[start2]:
            start += 1
        else:
            temp_value = y_arr[start2]
            index = start2
            while index > start:
                y_arr[index] = y_arr[index-1]
                index -= 1
                yield y_arr
            y_arr[start] = temp_value

            start += 1
            start2 += 1
    
def mergesort(y_arr, start, end):
    middle = (end+start)//2
    if (end - start+1) > 1:
        yield from mergesort(y_arr, start, middle)
        yield from mergesort(y_arr, middle+1, end)
        yield from merge(y_arr, start, middle, end)
        yield y_arr

def quicksort(y_arr, start, end):
    pivot = y_arr[start]; storeposition = start

    for i in range(start+1, end+1):
        if y_arr[i] < y_arr[start]:
            swap(y_arr, i, storeposition+1)
            storeposition += 1
            yield y_arr
    swap(y_arr, start, storeposition)
    yield y_arr

    if start != storeposition:
        yield from quicksort(y_arr, start, storeposition-1)
    if end != storeposition:
        yield from quicksort(y_arr, storeposition+1, end)
    
if __name__ == "__main__":
    user_in = int(input("Enter the sorting algorithm to use:\n(1) Bubble Sort\n(2) Selection Sort\n(3) Insertion Sort\n(4) Merge Sort\n(5) Quick Sort\n"))
    x = int(input("How much number do you want to randomly generate?\n"))

    # how many numbers to generate
    x_length = x
    # the height range of the bar plots
    y_min = 1
    y_max = 100
    # width of each bars
    bar_width = 1

    # y_arr is a randomly generated list of numbers that represent the bar's heights
    y_arr = np.array([np.random.randint(y_min, y_max) for _ in range(x_length)])
    # x_ arr is a list from 0 - x_length
    x_arr = np.array([i for i in range(x_length)])

    if user_in == 1:
        generator = bubblesort(y_arr)
        title = 'Bubble Sort'
    elif user_in == 2:
        generator = selectionsort(y_arr)
        title = 'Selection Sort'
    elif user_in == 3:
        generator = insertionsort(y_arr)
        title = 'Insertion Sort'
    elif user_in == 4:
        generator = mergesort(y_arr, 0, len(y_arr)-1)
        title = 'Merge Sort'
    elif user_in == 5:
        generator = quicksort(y_arr, 0, len(y_arr)-1)
        title = 'Quick Sort'

    fig=plt.figure()
    bar = plt.bar(x_arr, y_arr, width=bar_width, edgecolor='white', align='center')
    plt.axis('off')
    plt.title(title)

    def animate(heights, bar, color):
        for bar, height in zip(bar, heights):
            bar.set_height(height)
        return

    anim=animation.FuncAnimation(fig,func=animate,repeat=False,frames=generator,interval=1,fargs=(bar, color))

    plt.show()