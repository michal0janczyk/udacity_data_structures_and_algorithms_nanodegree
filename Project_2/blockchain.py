#! usr/bin/env python3

import time
import hashlib


class Block:
    def __init__(self, data, previous_hash) -> None:
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self.calc_hash()

    def __repr__(self) -> str:
        return "\n Block contains \
        \n Data: {0} \
        \n Timestamp: {1} \
        \n Hash: {2}".format(
            self.data, self.timestamp, self.hash
        )

    def get_previous_hash(self):
        return self.hash

    def get_data(self):
        return self.data

    @staticmethod
    def calc_hash() -> str:
        sha = hashlib.sha256()
        hash_str = "We are going to huffman_encoding this string of data!".encode(
            "utf-8"
        )
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def get_data(self):
        return self.head.get_data()

    def get_size(self):
        """
        Return the size or length of the linked list

        Returns:
            [type] -- [description]
        """
        return self.size

    def to_list(self):
        """
        Transforms the BlockChain content into a list

        Returns:
            [type] -- [description]
        """
        out = []
        block = self.head
        while block:
            out.append(block.data)
            block = block.previous_block
        return out

    def prepend(self, data) -> Block:
        """
        Prepend a data to the beginning of the list

        Arguments:
            data {[Block]} -- [new block in chain]
        """
        if self.head is None:
            self.head = Block(data, None)
            return

        new_head = Block(data, self.head.get_previous_hash())
        new_head.previous_block = self.head
        self.head = new_head
        self.size += 1
        return

    def append(self, data):
        """
        Append a data to the end of the list

        Arguments:
            data {[type]} -- [new data]
        """
        if self.head is None:
            self.head = Block(data, None)
        else:
            previous_block = self.head
            previous_hash = previous_block.get_previous_hash()
            new_block = Block(data, previous_hash)
            new_block.previous_block = previous_block
            self.head = new_block

        self.size += 1
        return

    def search(self, data):
        """
        Search the linked list for a Node with the requested data
        and return the Node

        Arguments:
            data {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        if self.head is None:
            return None

        block = self.head
        while block:
            if block.data == data:
                return block
            block = block.previous_block

        raise ValueError("Data not found in the list.")


def main():

    # Test prepend
    block_chain = BlockChain()
    block_chain.prepend(1)
    assert block_chain.to_list() == [1], f"list contents: {block_chain.to_list()}"

    # Test append - 1
    block_chain.append(3)
    block_chain.prepend(2)
    assert block_chain.to_list() == [2, 3, 1], f"list contents: {block_chain.to_list()}"

    # Test append - 2
    block_chain = BlockChain()
    block_chain.append(1)
    assert block_chain.to_list() == [1], f"list contents: {block_chain.to_list()}"
    block_chain.append(3)
    assert block_chain.to_list() == [3, 1], f"list contents: {block_chain.to_list()}"

    # Test search
    block_chain.prepend(2)
    block_chain.prepend(1)
    block_chain.append(4)
    block_chain.append(3)
    assert block_chain.search(1).data == 1, f"list contents: {block_chain.to_list()}"
    assert block_chain.search(4).data == 4, f"list contents: {block_chain.to_list()}"

    # Test size function
    assert block_chain.get_size() == 6, f"list contents: {block_chain.to_list()}"


if __name__ == "__main__":
    main()
