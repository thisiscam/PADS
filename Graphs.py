"""Graphs.py

Various simple functions for graph input.

Each function's input graph G should be represented in such a way that "for v in G" loops through the vertices, and "G[v]" produces a list of the neighbors of v; for instance, G may be a dictionary mapping each vertex to its neighbor set.

D. Eppstein, April 2004.
"""

from sets import Set

def isUndirected(G):
    """Check that G represents a simple undirected graph."""
    for v in G:
        if v in G[v]:
            return False
        for w in G[v]:
            if v not in G[w]:
                return False
    return True

def maxDegree(G):
    """Return the maximum vertex (out)degree of graph G."""
    return max([len(G[v]) for v in G])

def minDegree(G):
    """Return the minimum vertex (out)degree of graph G."""
    return min([len(G[v]) for v in G])

def copyGraph(G,adjacency_list_type=Set):
    """
    Make a copy of a graph G and return the copy.
    Any information stored in edges G[v][w] is discarded.
    The second argument should be a callable that turns a sequence
    of neighbors into an appropriate representation of the adjacency list.
    Note that, while Set, list, and tuple are appropriate values for
    adjacency_list_type, dict is not -- use Util.map_to_constant instead.
    """
    return dict([(v,adjacency_list_type(iter(G[v]))) for v in G])
