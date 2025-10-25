import Heap


def HeapSort(lst):
    """
    sort the element in max heap in ascending order.
    """

    n = len(lst)
    Heap.build_heap(lst)

    for i in reversed(range(n)):
        lst[i], lst[0] = lst[0], lst[i]
        Heap.heapify(lst, i, 0)
        # always heapify the root node by considering the only unsorted elements
        # as in heap root is always greater therefore we are swapping
        # the root to the last of list as the larger element sits there as we sorting in ascending order


HeapSort(Heap.binary_tree)

print(Heap.binary_tree)
