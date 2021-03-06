"""
Simple graph implementation
"""
import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node, visited=None):        
        if visited is None:            
            visited = []
        visited.append(starting_node)  
        print(starting_node)   
        
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited
    def bft(self, starting_node):
        visited = []
        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:  
            dequeued = q.dequeue() 
            visited.append(dequeued)  
            print(dequeued)
            for edge in self.vertices[dequeued].edges: 
                if edge not in visited:  
                    q.enqueue(edge) 
        return visited
    def dfs(self, starting_node, target=None):
        visited = []
        s = Stack()
        s.push(starting_node)
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                if current == target:
                    visited.append(current)
                    break
                visited.append(current)
                for next_vert in self.vertices[current].edges:
                    s.push(next_vert)
        print(visited)
        return visited
        
    def bfs(self, starting_node, target):
        visited = set()
        q = Queue()
        q.enqueue([starting_node])
        while q.size() > 0:  
            node = q.dequeue()
            if node[-1] not in visited: 
                if target == node[-1]:
                    return node
                visited.add(node[-1])            
                for child in self.vertices[node[-1]].edges: 
                    new_path = list(node)
                    new_path.append(child)
                    q.enqueue(new_path)
        return None


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()
