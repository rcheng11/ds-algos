

'''
Design a matrix implementation of a Graph with the functions
- run_bfs(v), uses breadth first search to check if v
- run_dfs(v), uses depth first search
- count_paths(), which counts the number of paths in the graph 
'''

class MatrixGraph:
    def __init__(self, matrix):
        '''
        The matrix is a 2D square array with n and m = |V|
        Each row in the matrix represents a vertex
            The column at that row represents whether there is a directed edge
            from that row's vertex to that column's vertex. (1 if edge, 0 if not)
        
        Ex:
        [0 0 1]
        [0 0 1]
        [1 0 0]
        1 -- 3 <-- 2
        '''
        self.matrix = matrix

    def run_bfs(self, s: int, v: int) -> bool:
        '''Runs BFS on the Graph object. Returns True if s reaches v, False otherwise.
        Implementation Notes: Start from s, go one vertex away at a time until all are visited
            Base Cases:
            Logic:
        Runtime: 
        '''
        visited = []

        while len(visited) < len(self.matrix):
            pass

    def run_dfs(self, s: int, v: int) -> bool:
        '''Runs DFS on the Graph object. Returns True if s reaches v, False otherwise.
        Implementation Notes:
            Base Cases:
            Recursive Relation:
            Logic:
        Runtime: 
        '''
        pass

    def count_paths(self, v: int) -> int:
        '''Counts the number of paths on the Graph object.
        Implementation Notes:
            Base Cases:
            Recursive Relation:
            Logic:
        Runtime: 
        '''
        pass

    def sort_degree(self, s: int) -> list[int]:
        '''Returns a list of tuples representing vertices
        as integers on the matrix by ascending order of the
        degree of the vertex in the graph from a source
        vertex s.
        Implementation Notes: 
            Base Cases:
            Logic:
        Runtime: 
        '''
