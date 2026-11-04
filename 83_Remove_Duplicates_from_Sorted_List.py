問題：ソート済みの単方向結合リストの先頭headが与えられる。重複した要素を削除して、ソートされたリストを返す。

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

AttributeError: 'Solution' object has no attribute 'deleteDuplicates'
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().deleteDuplicates(param_1)
Line 43 in _driver (Solution.py)
    ~~~~~~~^^
    _driver()
Line 58 in <module> (Solution.py)
