"""Quick Sort implemented from scratch.

Returns:
    (sorted_values, comparisons)

The comparison counter counts each element-to-pivot comparison.
This implementation uses three-way partitioning and additional lists,
so it is not an in-place Quick Sort.
"""

import random


def quick_sort(values):
    comparisons = 0

    def sort(items):
        nonlocal comparisons

        if len(items) <= 1:
            return items

        # Choose a random pivot to reduce the chance of highly
        # unbalanced partitions on already-sorted or reverse-sorted data.
        pivot = random.choice(items)

        left = []
        middle = []
        right = []

        for item in items:
            if item < pivot:
                comparisons += 1
                left.append(item)
            elif item > pivot:
                comparisons += 2
                right.append(item)
            else:
                # Both comparisons were false, so item equals the pivot.
                # Count the two element-to-pivot comparisons consistently.
                comparisons += 2
                middle.append(item)

        return sort(left) + middle + sort(right)

    return sort(values), comparisons


if __name__ == "__main__":
    sample = [8, 3, 7, 1, 9, 2, 5, 5]
    sorted_values, comparison_count = quick_sort(sample)

    print("Original dataset:", sample)
    print("Sorted dataset:  ", sorted_values)
    print("Comparisons:     ", comparison_count)
