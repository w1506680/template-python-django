from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
apple_count = fruits.count("apple")
print(apple_count)

print(fruits.index('apple'))

print(fruits.index('apple', 2))

fruits.reverse()

print(fruits)

stack = [3, 4, 5]

stack.append(6)
stack.append(7)

print(stack)

stack.pop()

print(stack)

q = deque(["Carrot", "Tomato", "Potato", "Beetroot"])
q.popleft()
print(q)

q.append("Radish")
print(q)

squares = [x**2 for x in range(10)]
print(squares)