from LinkedListProblems.linkedList import Node, LinkedList


def remove_elements(head, val):
    current_node = head
    dummy_node = None

    while current_node:

        if current_node.val != val:
            new_node = Node(current_node.val)

            if dummy_node is None:
                dummy_node = new_node

            else:
                last_node = dummy_node
                while last_node.next:
                    last_node = last_node.next

                last_node.next = new_node

        current_node = current_node.next

    return dummy_node


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(7)
    linkedList.append(7)
    linkedList.append(7)
    linkedList.append(7)
    linkedList.append(7)
    linkedList.append(6)

    linkedList.print_node()

    nodeList = linkedList.return_linked_list()

    removedList = remove_elements(nodeList, 7)

    while removedList:
        print(removedList.val, end="->")
        removedList = removedList.next

    print(None)
