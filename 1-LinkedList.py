class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # constructor to initialize LinkedList
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # helper method to print LinkedList
    def print_list(list):
        temp = list.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # method to append a new node
    def append(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # method to pop the tail node
    def pop(self):
        if (self.length == 0):
            return None

        temp = self.head
        pre = self.head
        if (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if (self.length == 0):
            self.head = None
            self.tail = None

        return temp

    # method to prepend to beginning of LinkedList
    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # method to pop the tail node
    def pop_first(self):
        if (self.length == 0):
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if (self.length == 0):
            self.tail = None

        return temp

    # get item using an index
    def get(self, index):
        if (index < 0 or index >= self.length):
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # set item using an index
    def set_value(self, index, value):
        temp = self.get(index)
        if (temp):
            temp.value = value
            return True
        return False

    # insert item at an index
    def insert(self, index, value):
        if (index < 0 or index >= self.length):
            return False

        if (index == 0):
            return self.prepend(value)

        if (index == self.length):
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # remove item at an index
    def remove(self, index):
        if (index < 0 or index >= self.length):
            return None

        if (index == 0):
            return self.pop_first()

        if (index == self.length):
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # reverse a LinkedList
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
# my_linked_list.append(4)
my_linked_list.print_list()
print(' ')

my_linked_list.reverse()
print(' ')

print(my_linked_list.find_middle().value)
