import heapq


H = [21, 1, 45, 78, 3, 5]
# push the smallest to the front
heapq.heapify(H)
print(H)

# add element
heapq.heappush(H, 8)
print(H)

# remove element
print(heapq.heappop(H))
print(H)

# replace the smallest element
print(heapq.heapreplace(H, 6))
print(H)


H = [(4, 'a'), (3, 'b'), (2, 'c')]
heapq.heapify(H)
print(H)

heapq.heappush(H, (5, 'e'))
print(H)

print(heapq.heappop(H))
