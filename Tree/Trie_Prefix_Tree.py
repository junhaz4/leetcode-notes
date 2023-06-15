"""
A Trie or Prefix Tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
One important property is that all the descendants of a node have a common prefix of the string associated with that node.
It has three main applications:
1. Insert: Inserts the string word into the trie
2. Search: Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
3. startsWith: Returns true if there is a previously inserted string word that has the input prefix, and false otherwise.
"""
class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode() # no child in the current tree then create a new node for it
            cur = cur.child[w]
        cur.is_end = True

    def find(self,prefix):
      cur = self.root
      for c in prefix:
        if c not in cur.child:
          return False
        cur = cur.child[c]
      return cur
    
    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not False and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not False

    def delete(self, word):
        return self._delete(self.root, word, 0)

    def _delete(self, current, word, i):
        if i == len(word):
            if not current.is_end:
                return False
            current.is_end = False
            return len(current.map) == 0
        char = word[i]
        if char not in current.child:
            return False
        next_delete = self._delete(current.child[char], word, i + 1)
        if next_delete:
            del current.child[char]
            return len(current.child) == 0
        return False


# insert 
# time complexity: O(m) m is the length of key/word. In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only m operations.
# space complexity: O(m). In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add m new nodes, which takes us
# search/startwith
# time complexity: O(m) In each step of the algorithm we search for the next key character. In the worst case the algorithm performs m operations.
# space complexity: O(1)

"""
class Trie(object):            
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        p = self.root
        for c in word:            
            if c not in p: 
                p[c] = {}
            p = p[c]
        p['#'] = True  # mark the end of the word
 
    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node
        
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None
    
    def find(self, prefix):
        p = self.root
        for c in prefix:            
            if c not in p: return None
            p = p[c]
        return p
"""

"""
class Trie(object):
    class TrieNode(object):
        def __init__(self):
            self.is_word = False
            self.children = [None] * 26
        
    def __init__(self):
        self.root = Trie.TrieNode()
        
 
    def insert(self, word):
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]: 
                p.children[index] = Trie.TrieNode()
            p = p.children[index]
        p.is_word = True
 
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word
        
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None
    
    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not p.children[index]: return None
            p = p.children[index]
        return p
        
        
        
    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \
                    children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)
        self.delete_helper(key, self.root, len(key), 0)
"""