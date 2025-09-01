from collections import deque
from queue import LifoQueue

stack= LifoQueue()

stack.put("Eat")
stack.put("rise")

print(stack.empty())    #stack empty or not return true or false value

top=stack.get()
print(top)
stack.put(top)