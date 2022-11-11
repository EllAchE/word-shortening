import csv

from Trie import Trie

def makeMappings(path):
    trie = Trie()

    count = 0
    # with open('./unigram_freq_words_only.csv') as f:
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            trie.insert(row[0], count)
            count += 1

    with open('./mappings.csv', 'w') as f:
        writer = csv.writer(f)

        # titles
        writer.writerow(["from", "to", "letters saved", "percentage of word saved", "word precedence"])

        # not a word and has a unique path should return the prefix -> prefix + full unique path suffix
        def dfs(node, prefix):
            if len(node.children) == 0:
                return node.char
            currPre = prefix + node.char
            if len(node.children) == 1:
                for child in node.children.values():
                    suffix = dfs(child, currPre)
                    from_chars = currPre + suffix[0]
                    to_chars = currPre + suffix
                    if not node.is_word:
                        return node.char + suffix
                    if len(suffix) > 1:
                        lettDiff = len(to_chars) - len(from_chars)
                        lettRat = lettDiff / len(to_chars)
                        writer.writerow([from_chars, to_chars, lettDiff, lettRat, trie.getFreq(to_chars)])
                    return node.char
            else:
                for child in node.children.values():
                    suffix = dfs(child, currPre)
                    if len(suffix) > 1:
                        from_chars = currPre + suffix[0]
                        to_chars = currPre + suffix
                        lettDiff = len(to_chars) - len(from_chars)
                        lettRat = lettDiff / len(to_chars)
                        writer.writerow([from_chars, to_chars, lettDiff, lettRat, trie.getFreq(to_chars)])
                return node.char

        dfs(trie.root, "")
