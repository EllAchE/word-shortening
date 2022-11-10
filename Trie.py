

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_word = True

    # def dfs(self, node, prefix):
    #     """Depth-first traversal of the trie
    #
    #     Args:
    #         - node: the node to start with
    #         - prefix: the current prefix, for tracing a
    #             word while traversing the trie
    #     """
    #     if node.is_end:
    #         self.output.append((prefix + node.char))
    #
    #     for child in node.children.values():
    #         self.dfs(child, prefix + node.char)