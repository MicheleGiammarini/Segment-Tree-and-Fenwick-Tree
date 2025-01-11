class SegmentTree:
  def __init__(self, arr):
      self.n = len(arr)
      self.tree = [0] * (2 * self.n)
      self.build(arr)

  def build(self, arr):
      # Initialize the leaves of the tree
      for i in range(self.n):
          self.tree[self.n + i] = arr[i]

      # Build the internal nodes by combining the leaves
      for i in range(self.n - 1, 0, -1):
          self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

  def update(self, idx, value):
      # Update the value at index `idx` to `value`
      idx += self.n
      self.tree[idx] = value

      # Recalculate the internal nodes
      while idx > 1:
          idx //= 2
          self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

  def query(self, left, right):
      # Query the sum of the elements between indices `left` and `right` (inclusive)
      left += self.n
      right += self.n
      result = 0

      while left <= right:
          if left % 2 == 1:  # If `left` is a right child
              result += self.tree[left]
              left += 1
          if right % 2 == 0:  # If `right` is a left child
              result += self.tree[right]
              right -= 1
          left //= 2
          right //= 2
      return result

# Example Usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query the sum from index 1 to 3
print(seg_tree.query(1, 3))  # Output: 15 (3 + 5 + 7)

# Update the value at index 1 to 10
seg_tree.update(1, 10)

# Query again the sum from index 1 to 3
print(seg_tree.query(1, 3))  # Output: 22 (10 + 5 + 7)
