class Node:
    def __init__(self,v):
            self.left=None
            self.right=None
            self.data=v 

root=Node(100)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(70)
root.right.left=Node(50)
root.right.right=Node(90)


def inorder(root):
      if root:
            inorder(root.left) 
            print(root.data) 
            inorder(root.right)



def preorder(root):
        if root:
              print(root.data) 
              preorder(root.left) 
              preorder(root.right)

def postorder(root):
        if root:
               postorder(root.left) 
               postorder(root.right) 
               print(root.data) 



uinput=input("What Operation should do you choose? Inorder, Preorder, or Postorder?   ")

if uinput ==  "Inorder" or uinput == "inorder":
    print("Inorder Traversal")
    inorder(root)
elif uinput == "Preorder" or uinput == "preorder":
    print("Preorder Traversal")
    preorder(root)
elif uinput == "Postorder" or uinput == "postorder":
    print("Postorder Traversal")
    postorder(root)




