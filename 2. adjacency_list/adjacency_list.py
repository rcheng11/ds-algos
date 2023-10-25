class AdjacencyGraph:
    """Represents a Graph through an hash map.
    Each list in the 2d array represents the connecting edges.
    Assume edges are directed.
    For example:
    {"A" : [1],
     "B" : [0, 3],
     "C" : [1, 3],
     "D" : [2] }
    Represents this graph
    A <---> B ----> C
            ^~ D <-~^
    """
    def __init__(self, edges: list[list[str]]):
        '''Create an instance of an adjacency graph
        given a list of edges as strings.
        '''
        self.alst = {}
        for v1, v2 in edges: # list unpacking, ex. if ["A", "B"], v1="A" & v2="B"
            pass

        self.vnum = len(self.alst.keys())
    
    def run_dfs(self, s: str, v: str) -> bool:
        '''Runs a depth first search, returning True if s can reach v, 
        and False otherwise.
        '''
        pass

    def run_bfs(self, s: str, v: str) -> bool:
        '''Runs a breadth first search returning True if s can reach v, 
        and False otherwise.
        '''
        pass
    
    def shortest_path(self) -> list[str]:
        '''Returns the shortest path from s to any vertex as a list of ints.
        '''
        pass