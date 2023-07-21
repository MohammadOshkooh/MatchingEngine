class Heap:

    def heapify(self, heap, n, i, heap_type):
        """

        :param heap_type: max or min
        :param heap:
        :param n: number of nodes
        :param i: current node
        :return:
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2

        if heap_type == 'max':
            # See if left child of root exists and is greater than root
            if left < n and heap[largest] > heap[left]:
                largest = left

            # See if right child of root exists and is greater than root
            if right < n and heap[largest] > heap[right]:
                largest = right

        elif heap_type == 'min':
            # See if left child of root exists and is greater than root
            if left < n and heap[largest] < heap[left]:
                largest = left

            # See if right child of root exists and is greater than root
            if right < n and heap[largest] < heap[right]:
                largest = right

        # Change root, if needed
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]  # swap

            # Heapify the root
            self.heapify(heap, n, largest, heap_type)

    def heapsort(self, heap, heap_type):
        """ Create a sorted heap"""
        length = len(heap)

        # Build a max heap.
        for i in range(length // 2 - 1, -1, -1):
            self.heapify(heap, length, i, heap_type)

        # One by one extract elements
        for i in range(length - 1, 0, -1):
            heap[i], heap[0] = heap[0], heap[i]  # swap
            self.heapify(heap, i, 0, heap_type)
