import heapq
import json

from heap import Heap


class MatchingEngine():

    def __init__(self, **kwargs):
        # create a heap instance
        self.heap = Heap()

        # Creating empty heap
        super().__init__(**kwargs)
        self.seller_min_heap = []  # min heap
        heapq.heapify(self.seller_min_heap)

        self.buyers_max_heap = []  # max heap
        heapq.heapify(self.buyers_max_heap)

        # load
        with open('app/api/sellers_data.json') as file:
            sellers_data = json.load(file)
            for element in sellers_data:
                heapq.heappush(self.seller_min_heap, (element.get('price'), element))

        with open('app/api/buyers_data.json') as file:
            buyers_data = json.load(file)
            for element in buyers_data:
                heapq.heappush(self.buyers_max_heap, (element.get('price'), element))

        self.heap.heapsort(self.buyers_max_heap, heap_type='max')
        self.heap.heapsort(self.seller_min_heap, heap_type='min')

    def matching_engine(self, data):
        request_type = data['type']
        current_heap = self.seller_min_heap if request_type == 'sell' else self.buyers_max_heap
        other_heap = self.buyers_max_heap if request_type == 'sell' else self.seller_min_heap

        def comparison():
            if request_type == 'sell':
                return other_heap[0][1].get('price') >= data['price']
            elif request_type == 'buy':
                return other_heap[0][1].get('price') <= data['price']

        while other_heap[0][1].get('amount') > 0:
            if comparison():
                if other_heap[0][1].get('amount') <= data['amount']:
                    data['amount'] -= other_heap[0][1].get('amount')
                    heapq.heappop(other_heap)
                else:
                    other_heap[0][1].update(
                        amount=other_heap[0][1].get('amount') - data['amount'])
                    break
            else:
                heapq.heappush(current_heap, (data['price'], data))
                self.heap.heapsort(current_heap, heap_type='max')
                break

    @staticmethod
    def get_data(self):
        serialized_data = input()
        data = serialized_data
        data['amount'] = float(data['amount'])
        self.matching_engine(data)

