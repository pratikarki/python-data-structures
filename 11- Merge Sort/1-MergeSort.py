# helper method to merge two sorted list
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if (list1[i] < list2[j]):
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(list):
    # break list in half until len(list) is 1
    if (len(list) == 1):
        return list

    mid_index = int(len(list) / 2)
    left = merge_sort(list[:mid_index])
    right = merge_sort(list[mid_index:])

    # user helper merge() to join two sorted lists recursively
    return merge(left, right)


print(merge_sort([1, 2, 9, 6, 7, 8, 4, 0, 10, 13, 12, 14, 5, 15, 3, 11]))
