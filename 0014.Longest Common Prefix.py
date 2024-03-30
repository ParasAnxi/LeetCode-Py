class Solution:
    def isLcp(self, strs: List[str], length: int) -> bool:
      str1 = strs[0][:length]
      for i in range(1, len(strs)):
        if not strs[i].startswith(str1):
          return False
      return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
      if not strs:
        return ""
      minLen = float('inf')
      for st in strs:
        x = len(st)
        minLen = min(minLen, x)

      left, right = 0, minLen
      while left < right:
        mid = (left + right) // 2
        if self.isLcp(strs, mid + 1):
          left = mid + 1
        else:
          right = mid
      return strs[0][:left]
    
#Using Trie
    

class TrieNode:
  def __init__(self, ch):
    self.data = ch
    self.isTerminal = False
    self.children = [None] * 26


class Trie:
  def __init__(self):
    self.root = TrieNode('')

  def insert(self, word):
    curr = self.root
    for ch in word:
      index = ord(ch) - ord('a')
      if not curr.children[index]:
        curr.children[index] = TrieNode(ch)
      curr = curr.children[index]
    curr.isTerminal = True

  def lcp(self):
    curr = self.root
    ans = ''
    while curr:
      if curr.isTerminal or sum(x is not None for x in curr.children) != 1:
        break
      for i, child in enumerate(curr.children):
        if child:
          ans += chr(ord('a') + i)
          curr = child
          break
    return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      trie = Trie()
      for word in strs:
        trie. insert(word)
      return trie.lcp()
