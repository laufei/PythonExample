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
	queue = []
	queue.append(begin)
	seen = set()
	seen.add(begin)
	while(queue):
		key = queue.pop(0)
		value = graph[key]
		for v in value:
			if v not in seen:
				queue.append(v)
				seen.add(v)
		print key

BFS(graph, "A")

def DFS(graph, begin):
	stack = []
	stack.append(begin)
	seen = set()
	seen.add(begin)
	while(stack):
		key = stack.pop(-1)
		value = graph[key]
		for v in value:
			if v not in seen:
				stack.append(v)
				seen.add(v)
		print key

DFS(graph, "A")