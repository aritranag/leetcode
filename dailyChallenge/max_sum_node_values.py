
class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = Node(root)


def createTree(nums:list[int],edges: list[list[int]]):
    """
    @param n: Nodes in the list numbered 0 - n-1
    @param edges : List of edges, u,v (undirected edge)
    returns a tree object
    """
    # sort the edges themselves to make all of them start from a lower node to a higher node, parent to child
    for edge in edges:
        edge.sort()
    
    # sort the edges from top to bottom
    edges.sort(key = lambda x: x[0])

    tree = Tree(nums[0])
    for edge in edges:
        child = Node(edge[1])
        



def maxValueSum(nums:list[int],k:int,edges: list[list[int]]):
    """
    """

    edges.sort(key = lambda x: min(x[0],x[1]))

    for edge in edges:
        u, v = edge[0], edge[1]

        first_sum = nums[u] + nums[v]

        mod_u = nums[u] ^ k
        mod_v = nums[v] ^ k

        mod_sum = mod_u + mod_v

        if (mod_sum >= first_sum):
            nums[u] = mod_u
            nums[v] = mod_v

    result = sum(nums)

    return result

#print(maxValueSum([1,2,1],3,[[0,1],[0,2]]))
#print(maxValueSum([2,3],7,[[0,1]]))
#print(maxValueSum([7,7,7,7,7,7],3,[[0,1],[0,2],[0,3],[0,4],[0,5]]))
print(maxValueSum([78,43,92,97,95,94],6,[[1,2],[3,0],[4,0],[0,1],[1,5]]))