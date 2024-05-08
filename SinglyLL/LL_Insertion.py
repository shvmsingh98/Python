class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.next = None
    def empty(self):
        if self.next is None:
            print("empty")
            return
    def insertAtFirst(self,value):
        new_node = node(value)
        node.next = self.next
        self.next = new_node

    def insertAtLast(self,value):
        new_node = node(value)
        if not self.empty():
            temp = self.next
            while temp.next is not None:
                temp = temp.next
            temp.next =new_node
        else:
            self.next = node        

    def search(self,value):
        temp =self.next
        while temp is not None:
            if temp.value == value:
                print("yes")
            temp = temp.next
        print('no') 

    def printLL(self):
        temp=self.next
        while temp is not None:
            print(temp.value, end= " ")
            temp=temp.next

    def insertAtLoc(self,value,target_value):
        
        temp = self.next
        while temp is not None:
            if temp.value == value:
                new_node=node(target_value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp=temp.next
        print("nooooooooooooooo")  

    def delFirst(self):
        if self.empty():
            print("not possible")
        else:
            self.next = self.next.next

    def delatLast(self):
        if self.empty():
            print("no nodes")
        if self.next.next is None:
            self.next = None
            return
        temp = self.next
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None   

    def delatLoc(self,targetValue):
        if self.empty():
            print("Empty")
        if self.next.value ==targetValue:
            self.next = self.next.next
        prev = None
        temp = self.next
        while temp is not None and temp.value != targetValue:
            prev = temp
            temp = temp.next    
        if temp is not None:
            prev.next = temp.next
        else:
            print(f"Value {targetValue} not found in the list.")




MyList = SinglyLL()
MyList.insertAtFirst(20)
MyList.insertAtLast(45)
MyList.insertAtLast(4)
MyList.insertAtLast(50)
MyList.insertAtLast(75)
MyList.insertAtLoc(96,34)
MyList.printLL()
print()
MyList.delatLoc(45)
MyList.printLL()

