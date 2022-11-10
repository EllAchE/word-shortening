import csv

from Trie import Trie

trie = Trie()

# with open('./unigram_freq_words_only.csv') as f:
with open('./unigram_freq_words_only.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        trie.insert(row[0])

mapping = {}

# not a word and has a unique path should return the prefix -> prefix + full unique path suffix
def dfs(node, prefix):
    if len(node.children) == 0:
        return node.char
    currPre = prefix + node.char
    if len(node.children) == 1:
        for child in node.children.values():
            suffix = dfs(child, currPre)
            if not node.is_word:
                return node.char + suffix
            if len(suffix) > 1:
                mapping[currPre + suffix[0]] = currPre + suffix
            return node.char
    else:
        for child in node.children.values():
            suffix = dfs(child, currPre)
            if len(suffix) > 1:
                mapping[currPre + suffix[0]] = currPre + suffix
        return node.char

dfs(trie.root, "")

print(mapping)


# with open('./mappings.csv') as f:
#     writer = csv.writer(f)

