#! usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.element) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    out_list = LinkedList()
    union_set = set()
    node_1 = llist_1.head
    node_2 = llist_2.head

    while node_1:
        union_set.add(node_1.element)
        node_1 = node_1.next

    while node_2:
        union_set.add(node_2.element)
        node_2 = node_2.next

    for elem in union_set:
        out_list.append(elem)

    return out_list


def intersection(llist_1, llist_2):
    out_list = LinkedList()
    inter_set = set()
    node_1 = llist_1.head
    node_2 = llist_2.head

    while node_1:
        while node_2:
            if node_1.element == node_2.element:
                inter_set.add(node_1.element)
            node_2 = node_2.next
        node_1 = node_1.next
        node_2 = llist_2.head

    for i in inter_set:
        out_list.append(i)

    return out_list


def main():

    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


if __name__ == "__main__":
    main()
