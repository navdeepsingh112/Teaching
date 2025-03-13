def merge(l1, l2):
    # Initialize indices for both lists and the lengths
    i = 0
    j = 0
    n = len(l1)
    m = len(l2)
    l3 = []  # Merged list

    # Merge elements from both lists in sorted order
    while i < n and j < m:
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    # Add remaining elements from l2, if any
    while j < m:
        l3.append(l2[j])
        j += 1

    # Add remaining elements from l1, if any
    while i < n:
        l3.append(l1[i])
        i += 1
    return l3

def divide(l):
    n = len(l)
    # Base case: if the list has only one element, return it
    if n == 1:
        return l

    # Split the list into two halves
    dl1 = l[0:n//2]
    dl2 = l[n//2:n]

    # Recursively divide and merge the two halves
    mdl1 = divide(dl1)
    mdl2 = divide(dl2)

    # Debugging output to show the divided lists
    # print(mdl1, mdl2)

    # Merge the sorted halves
    ml = merge(mdl1, mdl2)

    # Debugging output to show the merged list
    # print(ml)

    return ml

# Example list to sort
L = [8, 7, 3, 2, 4, 5, 1, 6]

# Perform merge sort
sL = divide(L)

# Print the sorted list
print(sL)