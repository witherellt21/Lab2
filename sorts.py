"""
Author: YOUR NAME GOES HERE
File: sorts.py

Defines the selection sort and the quick sort.
"""
from tools import compare, getRandomList, show

def selectionSort(numbers):    
    pass

def bubbleSort(numbers):
    pass
    

def quickSort(numbers):
    pass
 
def mergeSort(numbers):
    pass


def main():
    # Tests first a random input, then a sorted input
    for testType in ["Random", "Sorted"]:
        
        # Displays if random or sorted
        print(testType.title().center(25 + (12 * (3)) + 1, "=") + "\n")
        
        # Uses HOF to determine the testSet
        if testType == "Random":
            testSet = getRandomList
            
        else:
            testSet = lambda x: list(range(x))
            
        # Displays all three metrics as described for this lab
        for test in ["time", "swaps", "comparisons"]:
            # Invokes compare for all sorts
            
            compare(["Selection", "Bubble", "Quick", "Merge", ],
                [selectionSort, bubbleSort, quickSort, mergeSort],
                [10,100,1000,10000],
                dataSet=testSet,
                counter={"comparisons" : 0, "swaps" : 0},
                compareType=test)
        
        print()

if __name__ == "__main__":
    main()
    #show(10, quickSort, getRandomList)
