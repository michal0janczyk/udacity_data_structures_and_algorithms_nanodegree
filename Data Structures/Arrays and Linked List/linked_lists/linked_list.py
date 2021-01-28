class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # Diplay content of the Linked List
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        # Add node to the end of the Linked List
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        pass

    def insert_after_node(self, prev_node, data):
        pass

    def delete_node(self, key):
        pass

    def delete_node_at_pos(self, pos):
        pass

    def len_iterative(self):
        pass

    def len_recursive(self, node):
        pass

    def swap_nodes(self, key_1, key_2):
        pass

    def print_helper(self, node, name):
        pass

    def reverse_iterative(self):
        pass

    def reverse_recursive(self):
        pass

    def merge_sorted(self, llist):
        pass

    def remove_duplicates(self):
        pass

    def print_nth_from_last(self, n, method):
        pass

    def rotate(self, k):
        pass

    def count_occurences_iterative(self, data):
        pass

    def count_occurences_recursive(self, node, data):
        pass

    def is_palindrome_1(self):
        pass

    def is_palindrome_2(self):
        pass

    def is_palindrome_3(self):
        pass

    def is_palindrome(self, method):
        pass

    def move_tail_to_head(self):
        pass

    def sum_two_lists(self, llist):
        pass


if __name__ == "__main__":

    llist1 = LinkedList()
    llist1.append(5)
    llist1.append(6)
    llist1.append(3)
    llist1.print_list()

    # llist2 = LinkedList()
    # llist2.append(8)
    # llist2.append(4)
    # llist2.append(2)

    # print(365 + 248)
    # llist1.sum_two_lists(llist2)
