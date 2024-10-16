def levelOrder(root):
    # If the root is None, return an empty list
    if not root:
        return []
    
    result = []  # List to store the level-order traversal
    queue = [root]  # Initialize queue with the root node
    
    # Perform the level-order traversal
    while queue:
        node = queue.pop(0)  # Get the node at the front of the queue
        result.append(node.val)  # Add the node's value to the result
        
        # If the node has a left child, add it to the queue
        if node.left:
            queue.append(node.left)
        
        # If the node has a right child, add it to the queue
        if node.right:
            queue.append(node.right)
    
    return result