
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # def printLL(self,head):
    #     if self.head == None:
    #         print("Linked List is empty")
    #     else:
    #         temp = head
    #         while temp.next is not None:
    #             print(temp.data)
    #             temp.next = next


class SinglyLL:
    def __init__(self):
        self.next=None

    def insertAtFirst(self,value):
        new_node = node(value)
        node.next = head.next
        head.next = node

    def traverse(self):
        if self.next is None:
            print("Linked List is empty")
        else:
            temp = head
            while temp.next is not None:
                print(temp.data)
                temp.next = next



head = SinglyLL()
node1 = node(30)
head.next =node1.next
node2 = node(40)

SinglyLL.insertAtFirst(50)












# obj2 = node(20)
# head.next=obj2
# obj3 = node(30)
# obj2.next = obj3
# obj4 = node(40)
# obj3.next = obj4

# obj5 = node(50)
# obj5.next = head.next
# head.next = obj2
