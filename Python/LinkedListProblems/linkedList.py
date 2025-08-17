class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def print_node(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end="->")
            current_node = current_node.next

        print("None")

    def return_linked_list(self):
        return self.head