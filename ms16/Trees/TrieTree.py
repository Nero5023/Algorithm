class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26
 
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        for i in range(n):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1: 
                    new_node.is_word = True
                p.children[ord(s[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(s[i]) - ord('a')]
                if i == n - 1:
                    p.is_word = True
                    return
    
    def search(self, s):
        """Judge whether s is in this trie."""
        
        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False   
    
if __name__ == '__main__':
    trie = Trie()
    trie.add('str')
    trie.add('acb')
    trie.add('acblde')
    print trie.search('acb')
    print trie.search('ac')
    trie.add('ac')
    print trie.search('ac')