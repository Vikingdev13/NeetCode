"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # Time: O(m) : where m is the length of the key
    # Space: O(m)
    def insert(self, word):
        """
        word: string
        return: None
        """
        currNode = self.root
        # iterate through each char of a string
        for ch in word:
            # if that char doesnt have a node, create one, else skip it since it already exists
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
        currNode.endOfWord = True

    # Time: O(m) : where m is the length of the key
    # Space: O(1)
    def search(self, word):
        """
        word: string
        return: Bool
        """
        currNode = self.root
        # iterate through each char in string
        for ch in word:
            # if the char doesn't exist return false, else it does and set the currNode to that char
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return currNode.endOfWord
        
    # Time: O(m) : where m is the length of the key
    # Space: O(1)
    def startsWith(self, prefix):
        """
        prefix: string
        return: Bool
        """
        currNode = self.root
        # iterate through each char in the string
        for ch in prefix:
            # if the char does not exist, return false
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return True