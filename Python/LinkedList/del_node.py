def delNode(node):

    cp=node.next     # copy the nex node of del_node
    node.data=cp.data   #replce the node data with copied data
    node.next=cp.next    # point the address to next of next