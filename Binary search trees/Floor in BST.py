#Function to return the floor of given number in BST.
def floor(root,x):
    # code here
    res = -1
    
    while root is not None:
        
        if root.data == x:
            return root.data
        
        elif root.data > x:
            root = root.left
        
        else:
            res = root.data
            root = root.right
            
    return res