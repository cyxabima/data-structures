def heapify(lst, n, root):
    """
    heapify the root elements of lst which have total n elements
    """

    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != root:
        # swap
        lst[root], lst[largest] = lst[largest], lst[root]
        # now value at largest index is of root so heapify that node again
        heapify(lst, n, largest)


def build_heap(lst):
    n = len(lst)
    for i in reversed(range(n // 2)):
        heapify(lst, n, i)
        # heapify each element from bottom to top
        # since it is complete binary tree so leave nodes are at least half of the non leaf node
        # heapify ing leave node is useless


binary_tree = [2, 51, 47, 74, 14, 7, 3, 102]
#                    2
#                  /   \
#                51     47
#                /\     /\
#               74 14  7  3
#               /
#             102
build_heap(binary_tree)

print(binary_tree)

# ============ After Making Heap ============
#                   102
#                  /   \
#                74     47
#                /\     /\
#               51 14  7  3
#               /
#              2
