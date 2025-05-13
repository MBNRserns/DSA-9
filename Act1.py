#Tree: left less than right
#Traversals - Inorder: 1. Left node    2. Action on current node    3. Right node
#Traversals - Preorder: 1. Action on current node    2. Left node    3. Right node
#Traversals - Postorder: 1. Left node    2. Right node    3. Action on current node

class Node:
    def __init__(self,v):
            self.left=None
            self.right=None
            self.data=v #parent node

#Creating tree
root=Node(100)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(70)
root.right.left=Node(50)
root.right.right=Node(90)

def inorder(root):
      if root:
            inorder(root.left) #1. most left node
            print(root.data) #2. action on top node
            inorder(root.right) #3. right node

print("Inorder Traversal")
inorder(root)

def preorder(root):
        if root:
              print(root.data) #1. action on top node
              preorder(root.left) #2. most left node
              preorder(root.right) #3. right node

print("Preorder Traversal")
preorder(root)

def postorder(root):
        if root:
               postorder(root.left) #1. most left node
               postorder(root.right) #2. right node
               print(root.data) #action on top node

print("Postorder Traversal")
postorder(root)