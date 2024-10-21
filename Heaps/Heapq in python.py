import heapq as hq

l = [5, 7, 1, 9, 3]

hq.heapify(l) # This function is used to convert the iterable into a heap data structure. i.e. in heap order.

# print(list(l))

hq.heappush(l, 4) # This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.

# print(list(l))

print(hq.heappop(l)) # This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.

print(hq.heappushpop(l, 6))

print(hq.heapreplace(l,-1))

print(hq.nlargest(1, l))

print(hq.nsmallest(1, l))