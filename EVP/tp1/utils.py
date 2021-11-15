def DFS(Graph, start, visited):
    # Set current node as visited
    visited[start] = True

    # For every node of the graph
    for i in range(Graph.shape[0]):
        if (Graph[start][i] > 0 and (not visited[i])):
            DFS(Graph,i, visited)


def pgcd(a, b):
    if( b==0 ):
        return a
    else:
        return pgcd(b, a%b)