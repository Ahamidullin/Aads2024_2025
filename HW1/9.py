import heapq
import sys

heap = []

with open('input.txt', 'r') as file:
    for command in file:
        command = command.strip()

        if command == "CLEAR":
            heap.clear()

        elif command.startswith("ADD "):
            _, n = command.split()
            n = int(n)
            heapq.heappush(heap, -n)

        elif command == "EXTRACT":
            if heap:
                max_element = -heapq.heappop(heap)
                print(max_element)
            else:
                print("CANNOT")
