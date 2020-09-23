
from collections import deque
from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    # tuple to compare and confirm it is the earliest ancestor, node and distance from starting_node
    stack.append((starting_node, 0))
    visited = set()
    earliestAncestor = (starting_node, 0)

    # traversing stack
    while len(stack) > 0:
        # recieving tuple, current node, distance from node
        curr = stack.pop()
        # placed in varibale so theyre easy to refernce
        currNode, distance = curr[0], curr[1]
        # add to visited
        visited.add(curr)

        # find out if node is terminal, no more ancestors
        if currNode not in graph:
            # if its key is not graph, they are terminal
            # check if node is earliest ancestor, update EA variable
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
            # if it's not the EA, it needs to keep traversing
            else:
                # ancestors/neighbors of current node
                for ancestor in graph[currNode]:
                    # if not in visited, append to stack
                    if ancestor not in visited:
                        stack.append((ancestor, distance + 1))
                        # distance + 1 to keep track
        # after its travesered, we return the correct value and see if EA found is ourselves (starting_node) or not
        return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1
        # if ourselves, return -1


def createGraph(edges):
    # every key added to dict will have default value set
    graph = defaultdict(set)
    # go thru all the edges to construct directed graph from child to parent
    for edge in edges:
        # ancestor will always be first in array
        ancestor, child = edge[0], edge[1]
        # adding to graph
        graph[child].add(ancestor)
    return graph
