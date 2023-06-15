from collections import deque
class MyStack:
    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n)
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.que_in = deque() # store all elements in stack
        self.que_out = deque() # only use when pop is called

    def push(self, x):
        # push x to the back of que1
        self.que_in.append(x)

    def pop(self):
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个

        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None
        for i in range(len(self.que_in)-1):
            self.que_out.append(self.que_in.popleft())
        self.que_in, self.que_out = self.que_out, self.que_in
        return self.que_out.popleft()

    def top(self):
        """
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可
        """
        if self.empty():
            return None
        return self.que_in[-1]

    def empty(self):
        return len(self.que_in) == 0 # only need to check que_in

# Optimization: only one queue is used
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self):
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self):
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que
