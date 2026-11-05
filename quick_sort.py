
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
