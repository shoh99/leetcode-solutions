from typing import Optional
from linkedList import Node, LinkedList

class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        current_node = head
        linked_list = []
        while current_node:
            linked_list.append(current_node)
            current_node = current_node.next

        lst_length = len(linked_list)
        mid = lst_length // 2

        mid_node = linked_list[mid]

        while mid_node:
            print(mid_node.val)
            mid_node = mid_node.next


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(1)
    # linkedList.append(2)
    # linkedList.append(3)
    # linkedList.append(4)
    # linkedList.append(5)
    # linkedList.append(6)

    input = linkedList.return_linked_list()

    solution = Solution()
    solution.middleNode(input)