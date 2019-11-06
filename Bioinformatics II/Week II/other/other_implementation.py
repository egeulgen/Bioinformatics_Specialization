from collections import defaultdict

def ParseAdjacencyList(Adj_list):
    from re import split
    adj_list = []
    for elem in Adj_list:
        temp = split(' -> ', elem)
        temp[1] = temp[1].split(',')
        for t in temp[1]:
            adj_list.append((int(temp[0]), int(t)))
    return adj_list

class Graph:
    """A directed graph whose nodes are any hashable objects."""
    def __init__(self, edges=()):
        """Create a directed graph from an iterable of edges."""
        self._nodes = set() # Set of nodes.
        self._out = defaultdict(set) # Map from node to set of out-neighbours.
        self._in = defaultdict(set) # Map from node to set of in-neighbours.
        for m, n in edges:
            self.add_edge(m, n)
    def __iter__(self):
        """Iterating over the graph yields its nodes."""
        return iter(self._nodes)
    def add_edge(self, m, n):
        """Add an edge from m to n."""
        self._nodes.add(m)
        self._nodes.add(n)
        self._out[m].add(n)
        self._in[n].add(m)
    def remove_edge(self, m, n):
        """Remove the edge from m to n."""
        self._out[m].remove(n)
        self._in[n].remove(m)
    def out_neighbours(self, node):
        """Return the set of out-neighbours of a node."""
        return self._out[node]
    def in_degree(self, node):
        """Return the number of edges ending at node."""
        return len(self._in[node])
    def out_degree(self, node):
        """Return the number of edges starting at node."""
        return len(self._out[node])
    def degree(self, node):
        """Return the number of edges incident to node in either direction."""
        return self.in_degree(node) + self.out_degree(node)

from collections import deque

def pick_any(iterable):
    """Return any item from iterable, or raise StopIteration if empty."""
    return next(iter(iterable))

class NoEulerianPath(Exception):
    """Exception raised when there is no Eulerian path."""

def eulerian_path(edges):
    """Return an Eulerian path in the directed graph with the given
    iterable of edges, or raise NoEulerianPath if there is no such path.
    """
    graph = Graph(edges)
    # Mapping from surplus of out-edges over in-edges to list of nodes
    # with that surplus.
    surplus = defaultdict(list)
    for node in graph:
        in_degree = graph.in_degree(node)
        out_degree = graph.out_degree(node)
        degree_surplus = out_degree - in_degree
        if abs(degree_surplus) > 1:
            raise NoEulerianPath("Node {} has in-degree {} and out-degree {}."
                                 .format(node, in_degree, out_degree))
        surplus[degree_surplus].append(node)
    # Find the starting point for the path.
    if len(surplus[1]) == len(surplus[-1]) == 0:
        # Any starting point will do.
        start = pick_any(graph)
    elif len(surplus[1]) == len(surplus[-1]) == 1:
        # Must start at a node with more out- than in-neighbours.
        start = pick_any(surplus[1])
    else:
        raise NoEulerianPath("Graph has {} odd-degree nodes."
                             .format(len(surplus[1]) + len(surplus[-1])))
    # We'll be following a series of edge-disjoint paths in the graph.
    # This is a mapping from a node to a deque of the paths starting
    # at that node, each path being a list of nodes. (The reason for
    # using a deque is so that we can process these paths in the order
    # that they were found.)
    paths = defaultdict(deque)
    # Nodes that have been visited but have unvisited out-neighbours.
    unfinished = set([start])
    while unfinished:
        # Pick any unfinished node to start the current path.
        node = pick_any(unfinished)
        path = [node]
        paths[node].append(path)
        # Keep choosing any neighbour and removing the edge just
        # traversed, until a dead end is reached.
        while graph.out_degree(node):
            neighbour = pick_any(graph.out_neighbours(node))
            graph.remove_edge(node, neighbour)
            if graph.out_degree(node) == 0:
                unfinished.remove(node)
            path.append(neighbour)
            unfinished.add(neighbour)
            node = neighbour
        else:
            unfinished.remove(node)
    # If there are any edges remaining, that means the graph was
    # disconnected.
    if any(graph.degree(node) for node in graph):
        raise NoEulerianPath("Graph is not connected.")
    # Concatenate the individual paths into one continuous path (using
    # the "stack of iterators" pattern).
    path = []
    stack = [iter(paths[start].popleft())]
    while stack:
        for node in stack[-1]:
            if paths[node]:
                stack.append(iter(paths[node].popleft()))
                break
            else:
                path.append(node)
        else:
            stack.pop()
    # Check that we concatenated all the paths.
    assert not any(paths.values())
    return path

# Adj_list = []
# file = open('example.txt')
# for line in file:
#     Adj_list.append(line.rstrip())
if __name__ == "__main__":
    import sys
    Adj_list = sys.stdin.read().splitlines()
    edges = ParseAdjacencyList(Adj_list)
    res = eulerian_path(edges)
    print('->'.join(map(str, res)))
