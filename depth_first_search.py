 
graph = { 
    "a":["b","c"],
    "b":["d"], 
    "d":[],
    "c":["e"],
    "e":["f","g"],
    "f":[],
    "g":[]
         }

def dfs_iterative(graph, root): 
    stack = [root] 
    while len(stack) > 0: 
        currentNode = stack.pop()
        print(currentNode) 
        for node in graph[currentNode]:
            stack.append(node)


def bfs(graph, root): 
    stack = [root] 
    while len(stack) > 0: 
        currentNode = stack.pop(0)
        print(currentNode) 
        for node in graph[currentNode]:
            stack.append(node)


def dfs_recursive(graph, root):
        print(root)
        for node in graph[root]:
            dfs_recursive(graph, node)

bfs(graph, "a")
