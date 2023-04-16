class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Empty heap")
        self.swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self.bubble_down(0)
        return min_val

    def bubble_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.swap(idx, parent_idx)
            self.bubble_up(parent_idx)

    def bubble_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest_child_idx = idx
        if (left_child_idx < len(self.heap) and
            self.heap[left_child_idx] < self.heap[smallest_child_idx]):
            smallest_child_idx = left_child_idx
        if (right_child_idx < len(self.heap) and
            self.heap[right_child_idx] < self.heap[smallest_child_idx]):
            smallest_child_idx = right_child_idx
        if smallest_child_idx != idx:
            self.swap(idx, smallest_child_idx)
            self.bubble_down(smallest_child_idx)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
