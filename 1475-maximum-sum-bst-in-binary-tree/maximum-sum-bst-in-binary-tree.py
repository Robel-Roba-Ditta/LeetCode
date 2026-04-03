# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 def maxSumBST(self,r:Optional[TreeNode])->int:
  self.m=0
  def f(n):
   if not n:
    return True,float('inf'),float('-inf'),0
   a,b,c,d=f(n.left)
   e,g,h,i=f(n.right)
   if a and e and c<n.val<g:
    s=d+i+n.val
    self.m=max(self.m,s)
    return True,min(b,n.val),max(h,n.val),s
   else:
    return False,0,0,0
  f(r)
  return self.m