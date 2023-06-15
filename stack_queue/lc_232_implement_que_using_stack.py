class MyQueue:
  def __init__(self):
    self.stack_in = []
    self.stack_out = []

  def push(self, x):
    self.stack_in.append(x)

  def pop(self):
    if self.empty():
      return None
    if self.stack_out == []:
      while self.stack_in:
        self.stack_out.append(self.stack_in.pop())
    return self.stack_out.pop()

  def peek(self):
    ans = self.pop()
    self.stack_out.append(ans)
    return ans

  def empty(self):
    return self.stack_in == [] and self.stack_out == []