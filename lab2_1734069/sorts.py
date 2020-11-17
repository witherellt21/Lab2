"""
Author: YOUR NAME GOES HERE
File: sorts.py

Defines the selection sort and the quick sort.
"""
from tools import compare, getRandomList, show


def selectionSort(lyst, counter = None):

    def swap( i, j ):
        """Exchanges the items at positions i and j."""
        # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
        # but the following code shows what is really going on
        temp = lyst[ i ]
        lyst[ i ] = lyst[ j ]
        lyst[ j ] = temp

    i = 0
    while i < len( lyst ) - 1:  # Do n – 1 searches

        minIndex = i  # for the smallest item
        j = i + 1
        while j < len( lyst ):  # Start a search
            if lyst[ j ] < lyst[ minIndex ]:
                if counter:
                    counter[ "comparisons" ] += 1
                minIndex = j
            j += 1
        if minIndex != i:  # Swap if necessary
            if counter:
                counter["swaps"] += 1
            swap( minIndex, i )
        i += 1
    return lyst


def bubbleSort(lyst, counter = None):

    def swap( i, j ):
        """Exchanges the items at positions i and j."""
        # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
        # but the following code shows what is really going on
        temp = lyst[ i ]
        lyst[ i ] = lyst[ j ]
        lyst[ j ] = temp

    n = len( lyst )
    while n > 1:  # Do n - 1 bubbles
        # Start each bubble
        i = 1
        while i < n:
            if lyst[ i ] < lyst[ i - 1 ]:  # Exchange if needed
                if counter:
                    counter[ "swaps" ] += 1
                    counter["comparisons"] += 1
                swap( i, i - 1 )
            i += 1
        n -= 1
    return lyst


def quickSort(lyst, counter = None):


    def swap( i, j ):
        """Exchanges the items at positions i and j."""
        # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
        # but the following code shows what is really going on
        temp = lyst[ i ]
        lyst[ i ] = lyst[ j ]
        lyst[ j ] = temp

    def partition( left, right ):
        """Shifts items less than the pivot to its left,
        and items greater than the pivot to its right,
        and returns the position of the pivot."""
        # Find the pivot and exchange it with the last item
        middle = (left + right) // 2
        pivot = lyst[ middle ]
        lyst[ middle ] = lyst[ right ]
        lyst[ right ] = pivot
        # Set boundary point to first position
        boundary = left
        # Move items less than pivot to the left
        for index in range( left, right ):
            if lyst[ index ] < pivot:
                if counter:
                    counter["comparisons"] += 1
                    counter[ "swaps" ] += 1
                swap( index, boundary )
                boundary += 1
        # Exchange the pivot item and the boundary item
        if counter:
            counter[ "swaps" ] += 1
        swap( right, boundary )
        return boundary

    def quicksortHelper( left, right ):
        """Partition lyst, then sort the left segment and
        sort the right segment."""
        if left < right:
            if counter:
                counter["comparisons"] += 1
            pivotLocation = partition( left, right )
            quicksortHelper( left, pivotLocation - 1 )
            quicksortHelper( pivotLocation + 1, right )

    quicksortHelper( 0, len(lyst) - 1) # Top-level call of helper
    return lyst


def mergeSort(lyst, counter = None):
    # lyst list being sorted
    # copyBuffer temporary space needed during merge

    # low = 0
    # high = len(lyst) - 1

    def mergeSortHelper( low, high ):
        # lyst list being sorted
        # copyBuffer temporary space needed during merge
        # low, high bounds of sublist
        # middle midpoint of sublist
        if low < high:
            if counter:
                counter["comparisons"] += 1
            middle = (low + high) // 2
            mergeSortHelper( low, middle )
            mergeSortHelper(  middle + 1, high )
            merge( low, middle, high )

    def merge( low, middle, high ):

        i1 = low
        i2 = middle + 1

        for i in range( low, high + 1 ):

            if i1 > middle:
                if counter:
                    counter[ "comparisons" ] += 1
                copyBuffer[ i ] = lyst[ i2 ]
                i2 += 1
            elif i2 > high:
                if counter:
                    counter[ "comparisons" ] += 1
                copyBuffer[ i ] = lyst[ i1 ]
                i1 += 1
            elif lyst[ i1 ] < lyst[ i2 ]:
                if counter:
                    counter[ "comparisons" ] += 1
                    counter[ "swaps" ] += 1
                copyBuffer[ i ] = lyst[ i1 ]
                i1 += 1
            else:
                if counter:
                    counter[ "comparisons" ] += 1
                    counter[ "swaps" ] += 1
                copyBuffer[ i ] = lyst[ i2 ]
                i2 += 1

        for i in range( low, high + 1 ):
            if counter:
                counter[ "swaps" ] += 1
            lyst[ i ] = copyBuffer[ i ]

    copyBuffer = list( lyst )
    mergeSortHelper( 0, len( lyst ) - 1 )

    return lyst


def main():
    # Tests first a random input, then a sorted input
    for testType in [ "Random", "Sorted" ]:

        # Displays if random or sorted
        print( testType.title().center( 25 + (12 * (3)) + 1, "=" ) + "\n" )

        # Uses HOF to determine the testSet
        if testType == "Random":
            testSet = getRandomList

        else:
            testSet = lambda x: list( range( x ) )

        # Displays all three metrics as described for this lab
        for test in [ "time", "swaps", "comparisons" ]:
            # Invokes compare for all sorts

            compare( [ "Selection", "Bubble", "Quick", "Merge", ],
                     [ selectionSort, bubbleSort, quickSort, mergeSort ],
                     [ 10, 100, 1000, 10000 ],
                     dataSet=testSet,
                     counter={ "comparisons": 0, "swaps": 0 },
                     compareType=test )

        print()


if __name__ == "__main__":
    main()
    #show(10, quickSort, getRandomList)
