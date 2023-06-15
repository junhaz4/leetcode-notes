class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        '''
        遇到两个维度权衡的时候，一定要先确定一个维度，再确定另一个维度,如果两个维度一起考虑一定会顾此失彼。
        局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性
        全局最优：最后都做完插入操作，整个队列满足题目队列属性
        '''
        people.sort(key=lambda x: (-x[0],x[1]))
        que = []
        for p in people:
            que.insert(p[1],p)
        return que