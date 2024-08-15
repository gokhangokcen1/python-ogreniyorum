import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        from collections import deque
        if root is None:
            return
            
        queue = deque([root])  

        while queue:
            current_level_size = len(queue)  
            current_level_values = []  

            for _ in range(current_level_size):
                node = queue.popleft()  
                current_level_values.append(node.data)  

                if node.left:
                    queue.append(node.left)  
                if node.right:
                    queue.append(node.right)  

            print(*current_level_values, sep=" ", end= " ")
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
