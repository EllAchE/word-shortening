

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}
        self.word_freq = None


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word, freq):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_word = True
        node.word_freq = freq

    # lazy way to do
    def getFreq(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]

        return node.word_freq
