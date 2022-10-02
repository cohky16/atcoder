import heapq
class MultiSet:
    def __init__(self):
        self.cnt_dict = {}
        self.rank_min = []
        self.rank_max = []

    def add(self, num):
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = cnt + 1
        heapq.heappush(self.rank_min, num)
        heapq.heappush(self.rank_max, -num)

    def erase(self, num, d):
        cnt = self.cnt_dict.get(num, 0)
        self.cnt_dict[num] = max(0, cnt - d)

    def get_max(self):
        while self.cnt_dict[-self.rank_max[0]] == 0:
            -heapq.heappop(self.rank_max)
        return -self.rank_max[0]

    def get_min(self):
         while self.cnt_dict[self.rank_min[0]] == 0:
             heapq.heappop(self.rank_min)
         return self.rank_min[0]

s = MultiSet()
q = int(input())
for i in range(q):
    query = input().split()
    q = query[0]
    if q == '1':
        x = int(query[1])
        s.add(x)
    elif q == '2':
        x,c = int(query[1]),int(query[2])
        s.erase(x, c)
    elif q == '3':
        print(s.get_max()-s.get_min())