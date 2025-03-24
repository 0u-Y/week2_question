class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    entry = (priority, item)
    self.heap.append(entry)
    self._sift_up(len(self.heap) - 1)

  def pop(self):
    if len(self.heap) > 1:
      self._swap(0, len(self.heap) - 1)
      _, item = self.heap.pop()
      self._sift_down(0)
      return item
    elif len(self.heap) == 1:
      _, item = self.heap.pop()
      return item
    else:
      return None

  def _sift_up(self, index):
    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[parent_index][0] > self.heap[index][0]:
        self._swap(parent_index, index)
        index = parent_index
      else:
        break

  def _sift_down(self, index):
    while True:
      left = 2 * index + 1
      right = 2 * index + 2
      smallest = index

      if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
        smallest = left
      if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
        smallest = right
      if smallest != index:
        self._swap(index, smallest)
        index = smallest
      else:
        break

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
