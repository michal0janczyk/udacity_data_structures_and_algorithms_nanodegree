#! usr/bin/env python3

import sys
from queue import PriorityQueue


class Node(object):
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, node):
        return self.char and node.char and self.char < node.char

    def __repr__(self):
        return f"{self.char} => {self.freq}"


class HuffmanTree(object):
    def __init__(self, data):
        self.priority_queue = PriorityQueue()
        self.data = data

    def frequency_count(self):
        char_count = {}

        for char in self.data:
            if char_count.get(char):
                char_count[char] += 1
            else:
                char_count[char] = 1
        return [(value, key) for key, value in char_count.items()]

    def build_huffman_tree(self, freq):
        if len(freq) == 1:
            node = Node(None, 0)
            self.priority_queue.put(node)

        for value in freq:
            node = Node(char=value[1], freq=value[0])
            self.priority_queue.put(node)

        while self.priority_queue.qsize() > 1:
            hp1 = self.priority_queue.get()
            hp2 = self.priority_queue.get()
            parent = Node()
            parent.left = hp1
            parent.right = hp2
            parent.freq = hp1.freq + hp2.freq
            self.priority_queue.put(parent)

        return self.priority_queue.get()

    def encode_string(self, node, encoding_string, codes):
        if not node:
            return False

        if codes is None:
            codes = {}
        if encoding_string is None:
            encoding_string = ""
        if node.char:
            codes[node.char] = encoding_string
        self.encode_string(node.left, encoding_string + "0", codes)
        self.encode_string(node.right, encoding_string + "1", codes)
        return codes

    def encode(self, codes):
        return "".join([codes[letter] for letter in self.data])

    def huffman_decoding(self, root, codes):
        node = root
        output = ""
        for char in self.encode_string(node, self.data, codes):
            if node.left is None and node.right is None:
                output += node.char
                node = root
            node = node.left if char == "0" else node.right
        output += node.char
        return output


def main():
    a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
    huffman = HuffmanTree(a_great_sentence)
    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    codes = {}
    frequencies = huffman.frequency_count()
    tree = huffman.build_huffman_tree(frequencies)
    codes = huffman.encode_string(tree, "", codes)
    encoded_string = huffman.encode(codes)
    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_string, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_string))

    decoded_data = huffman.huffman_decoding(tree, codes)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    main()
