#!/usr/bin/env python
import sys
class Node:
    def __init__(self, i, next_=None):
        self.i = i
        if next_:
            self.next_ = next_
        else:
            self.next_ = self

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, i):
        if not self.head:
            self.head = Node(i)
        else:
            cur = self.head

            while cur.next_ != self.head:
                cur = cur.next_

            tmp = Node(i, self.head)
            cur.next_ = tmp
        self.count += 1
    
    def print_(self):
        cur = self.head

        while cur.next_ != self.head:
            print cur.i,
            cur = cur.next_
        print cur.i,

    def remove(self, m):
        x = 1
        pre = self.head
        cur = self.head
        while self.count > 1:
            if x%m == 0:
                print cur.i,
                
                pre.next_ = cur.next_
                cur = cur.next_
                self.count -= 1
            else:
                pre = cur
                cur = cur.next_
            x += 1
        print cur.i

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n,m = [int(x) for x in test.strip().split(',')]
    cll = CircularLinkedList()
    for i in range(n):
        cll.add(i)
    cll.remove(m)
test_cases.close()
