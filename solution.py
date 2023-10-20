import time

class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def get_suffixes_start_indices(self, word):
        node = self.root
        suffix_indices = []
        for i in range(len(word)):
            if node.is_end_of_word:
                suffix_indices.append(i)
            node = node.children[word[i]]
        return suffix_indices

def find_longest_and_second_longest_compounded_words(file_path):
    """Finds the longest and second longest compounded words in a file.

    Args:
        file_path: The path to the file.

    Returns:
        A tuple containing the longest and second longest compounded words, or None
        if no compounded words are found.
    """

    trie = Trie()
    with open(file_path, "r") as f:
        for word in f:
            trie.insert(word)

    longest_compounded_word = None
    longest_compounded_word_length = 0
    second_longest_compounded_word = None
    second_longest_compounded_word_length = 0

    for word in trie.root.children:
        suffix_indices = trie.get_suffixes_start_indices(word)
        for i in suffix_indices:
            if i >= len(word):
                continue
            remaining_suffix = word[i:]
            if trie.search(remaining_suffix):
                compounded_word = word + remaining_suffix
                compounded_word_length = len(compounded_word)

                if compounded_word_length > longest_compounded_word_length:
                    longest_compounded_word = compounded_word
                    longest_compounded_word_length = compounded_word_length
                elif compounded_word_length > second_longest_compounded_word_length:
                    second_longest_compounded_word = compounded_word
                    second_longest_compounded_word_length = compounded_word_length

    return longest_compounded_word, second_longest_compounded_word

def main():
    file_path = "Input_01.txt"
    start_time = time.time()

    longest_compounded_word, second_longest_compounded_word = find_longest_and_second_longest_compounded_words(file_path)

    end_time = time.time()
    processing_time = end_time - start_time

    print("Longest compound word:", longest_compounded_word)
    print("Second longest compound word:", second_longest_compounded_word)
    print("Time taken to process file:", processing_time * 1000, "milli seconds")

if _name_ == "_main_":
    main()