from heapq import heappush, heappop
class maxint:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        return self.val > other.val
'''    
with open('median.txt') as f:
    content = f.readlines()
    data = [int(x.split()[0]) for x in content]
'''
data = [1,2,3,4,5]    
    
l_heap = [maxint(min(data[0],data[1]))]
h_heap = [max(data[0],data[1])]
median = [data[0], min(data[0],data[1])]
for i in data[2:]:   
    if i > l_heap[0].val:
        heappush(h_heap,i)
        if len(h_heap) > len(l_heap) + 1:
            heappush(l_heap, maxint(heappop(h_heap)))
    else:
        heappush(l_heap,maxint(i))
        if len(l_heap) > len(h_heap) + 1:
            heappush(h_heap, heappop(l_heap).val)
            
    if len(h_heap) == len(l_heap):
        median.append(min(h_heap[0], l_heap[0].val))
    elif len(h_heap) > len(l_heap):
        median.append(h_heap[0])
    else:
        median.append(l_heap[0].val)
        
    
    
    













