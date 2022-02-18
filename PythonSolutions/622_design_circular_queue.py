class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = Node()

    def printQueue(self):
        if self.head.next is None:
            print([])
            return
        cur = self.head.next
        printout = []
        while True:
            printout.append(cur.value)
            if cur.next == self.head.next:
                break
            cur = cur.next
        print(printout)
        
    def length(self):
        if self.head.next is None:
            return 0

        cur = self.head.next
        count = 0
        while True:
            count += 1
            if cur.next == self.head.next:
                break
            cur = cur.next
        return count
            

    def enQueue(self, value: int) -> bool:
        if self.length() == self.size:
            return False

        if self.head.next is None:
            cur = self.head
            new_node = Node(value)
            cur.next = new_node
            new_node.next = self.head.next
            return True

        cur = self.head.next
        while cur.next != self.head.next:
            cur = cur.next
        new_node = Node(value)
        cur.next = new_node
        new_node.next = self.head.next
        return True        
        


    def deQueue(self) -> bool:
        if self.head.next is None:
            return False

        if self.head.next.next == self.head.next:
            self.head.next = None
            return True

        tail = self.head.next

        while tail.next != self.head.next:
            tail = tail.next

        garbage = self.head.next 
        self.head.next = self.head.next.next
        tail.next = self.head.next
        garbage = None

        return True
        
        
    def Front(self) -> int:
        if self.head.next is None:
            return -1
        else:
            return self.head.next.value

    def Rear(self) -> int:
        if self.head.next is None:
            return -1
        else:
            cur = self.head.next
            while cur.next != self.head.next:
                cur = cur.next
            return cur.value

    def isEmpty(self) -> bool:
        if self.head.next is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return self.length() == self.size


if __name__ == "__main__":
    mCQ = MyCircularQueue(3)
    mCQ.enQueue(3)
    mCQ.enQueue(5)
    mCQ.enQueue(7)
    mCQ.deQueue()
    mCQ.deQueue()
    mCQ.deQueue()
    print(mCQ.deQueue())
    mCQ.printQueue()

