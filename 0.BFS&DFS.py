# coding: utf-8
graph = {
	"A": ["B", "C"],
	"B": ["A", "C", "D"],
	"C": ["A", "B", "D", "E"],
	"D": ["B", "C", "E", "F"],
	"E": ["C", "D"],
	"F": ["D"],
}

def BFS(graph, begin):
	"""广度优先使用队列实现"""
	pass

BFS(graph, "A")

def DFS(graph, begin):
	"""深度优先使用栈实现"""
	pass

DFS(graph, "A")