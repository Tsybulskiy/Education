import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def huffman_encoding(node, binary_string="", code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = binary_string
            return code

        huffman_encoding(node.left, binary_string + "1", code)
        huffman_encoding(node.right, binary_string + "0", code)
        return code