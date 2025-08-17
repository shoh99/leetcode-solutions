from linkedList import LinkedList, Node


def reverse_list(head: Node):
    lst = get_val_list(head)
    reversed_node = None

    for i in range(len(lst) - 1, -1, -1):
        val = lst[i]
        new_node = Node(val)
        if reversed_node is None:
            reversed_node = new_node
            continue

        last_node = reversed_node

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    return reversed_node


def get_val_list(node):
    node_list = []

    while node:
        node_list.append(node.val)
        node = node.next

    return node_list


def get_last_node_(head: Node):
    last_node = head

    while last_node.next and last_node.next.next is not None:
        last_node = last_node.next

    last_node = last_node.next
    last_val = last_node.val

    last_node.next = None
    print(last_val)


def main(head: Node):
    current_node = head
    get_last_node_(current_node)




if __name__ == "__main__":
    linedList = LinkedList()

    linedList.append(1)
    linedList.append(2)
    linedList.append(3)
    linedList.append(4)
    linedList.append(5)

    node = linedList.return_linked_list()
    main(node)

    # reverse_node = reverse_list(node)
    #
    # while reverse_node:
    #     print(reverse_node.val)
    #     reverse_node = reverse_node.next
