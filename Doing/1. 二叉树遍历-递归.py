# coding: utf-8
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def preTraverse(root):
	if root is None:
		return
	print root.value
	preTraverse(root.left)
	preTraverse(root.right)

def midTraverse(root):
	if root is None:
		return
	midTraverse(root.left)
	print root.value
	midTraverse(root.right)

def afterTraverse(root):
	if root is None:
		return
	afterTraverse(root.left)
	afterTraverse(root.right)
	print root.value

def level_queue(root):
	"""
	利用队列实现树的层次遍历
	"""
	if root is None:
		return

	queue = [root]
	while queue:
		n = queue.pop(0)
		print n.value
		if n.left:
			queue.append(n.left)
		if n.right:
			queue.append(n.right)

if __name__ == '__main__':
	root = Node(
        value='D',
        left=Node(
            value='B',
            left=Node(
                    value='A'
            ),
            right=Node(
                    value='C'
            )
        ),
        right=Node(
            value='E',
            right=Node(
                value='G',
                left=Node(
                        value='F'
                )
            )
        )
    )

	print('前序遍历：')
	preTraverse(root)
	print('\n')
	print('中序遍历：')
	midTraverse(root)
	print('\n')
	print('后序遍历：')
	afterTraverse(root)
	print('\n')
	print('层次遍历：')
	level_queue(root)