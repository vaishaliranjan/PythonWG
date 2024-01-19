from node import Node
class BinaryTree:
    def __init__(self, head : Node):
        self.head= head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if(current_node.value==new_node.value):
                raise ValueError("There cant be duplicate elements in a tree.")
            elif current_node.value>new_node.value:
                if current_node.left:
                    current_node=current_node.left
                else:
                    current_node.left=new_node
                    break
            else:
                if current_node.right:
                    current_node=current_node.right
                else:
                    current_node.right=new_node
                    break

    def inorder(self):
        print("Inorder Traversal")
        self._inorder_traversal(self.head)

    def _inorder_traversal(self, current_node):
        if not current_node:
            return
        self._inorder_traversal(current_node.left)
        print(current_node.value)
        self._inorder_traversal(current_node.right)

    def preorder(self):
        print("Preorder Traversal")
        self._preorder_traversal(self.head)


    def _preorder_traversal(self, current_node):
        if not current_node:
            return
        print(current_node.value)
        self._preorder_traversal(current_node.left)
        self._preorder_traversal(current_node.right)

    def postorder(self):
        print("Postorder Traversal")
        self._postorder_traversal(self.head)

    def _postorder_traversal(self, current_node):
        if not current_node:
            return
        self._postorder_traversal(current_node.left)
        self._postorder_traversal(current_node.right)
        print(current_node.value)

    def find(self, value: int):
        current_node= self.head
        while current_node:
            if current_node.value==value:
                return current_node
            elif current_node.value> value:
                current_node=current_node.left
            else:
                current_node=current_node.right
        else:
            print("Value not found!!")

    def find_parent(self, value: int)-> Node:
        current_node= self.head
        if self.head and self.head.value==value:
            return self.head
        while current_node:
            if (current_node.left and current_node.left.value==value) or (current_node.right and current_node.right.value == value):
                return current_node
            elif value<current_node:
                current_node=current_node.left
            elif value>current_node:
                current_node = current_node.right

    def find_right_most(self, node: Node) -> Node:
        current_node= node
        while current_node.right:
            current_node=current_node.right
        return current_node

    def delete(self, value: int):
        to_delete= self.find(value)
        to_delete_parent=self.find_parent(value)

        if to_delete.right and to_delete.left:
            #two children
            right_most= self.find_right_most(to_delete.left)
            right_most_parent=self.find_parent(right_most.value)

            if right_most_parent !=to_delete:
                right_most_parent.right= right_most.left
                right_most.left= to_delete.right
            right_most.right= to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = right_most

            elif to_delete==to_delete_parent.right:
                to_delete_parent.right = right_most

            else:
                self.head=right_most


        elif to_delete.right or to_delete.left:
            #one child
            if to_delete == to_delete_parent.left:
                to_delete_parent.left= to_delete.left or to_delete.right
            elif to_delete==to_delete_parent.right:
                to_delete_parent.right=to_delete.left or to_delete.right
            else:
                self.head= to_delete.left or to_delete.right


        else:
            #no children
            if to_delete ==to_delete_parent.left:
                to_delete_parent.left=None
            elif to_delete==to_delete_parent.right:
                to_delete_parent.right=None
            else:
                self.head=None


