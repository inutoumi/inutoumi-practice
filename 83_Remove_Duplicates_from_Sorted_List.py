-問題：ソート済みの単方向結合リストの先頭headが与えられる。重複した要素を削除して、ソートされたリストを返す。


#1回目: 141,142で書いたコードを元に、自分で書いてみました。
-集合setは重複不可なので、要素をいったんsetに入れて重複を取り除き、そのあとソートし直そうと考えました。
```python
# Definition for singliy-sorted kist.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
    def noDuplicate(self, head: Optional[ListNode]) -> list:
        sortedList = set()
        element = head

        while element:
            if element in sortedList:
                sortedList.add(head)
            element = element.next
        
        return sortedList
```
```
AttributeError: 'Solution' object has no attribute 'deleteDuplicates'
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().deleteDuplicates(param_1)
Line 43 in _driver (Solution.py)
    ~~~~~~~^^
    _driver()
Line 58 in <module> (Solution.py)
```
-LeetCodeの右側に初めから表示されているコードは、回答ではなくてテンプレートだったことに気づきました。


#2回目: 他の方がAcceptしたコードを参考にしました。
https://github.com/olsen-blue/Arai60/pull/3/changes
-隣り合う2つのノードを見比べて、中身が重複していれば別のノードにつなぎ直すのはシンプルでわかりやすい。
-while node is not None and node.next is not None: の部分が理解するまで時間がかかった。
-while node and node.next: とも書き直せるようだけど、Noneもあることを忘れそうなので元のコードのままにした。

```python
# Definition for singly-linked list.
#   class __init__(self, val = 0, next = None):
#     self.val = val
#     self.next = next

class Solution:
    def deleteDuplicates(self, head : ListNode | None ):
        node = head
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
        return head
```

```python


