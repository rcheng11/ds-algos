

'''
Design a matrix implementation of a Graph with the functions
- run_bfs(v), uses breadth first search to check if v
- run_dfs(v), uses depth first search
- count_paths(), which counts the number of paths in the graph 
'''

class MatrixGraph:
    def __init__(self, matrix):
        '''
        0 represents free space, 1 represents blocked path.
        '''
        self.matrix = matrix

    def run_bfs(self, s: tuple, v: tuple) -> bool:
        '''Runs BFS on the Graph object. Returns True if s reaches v, False otherwise.
        Implementation Notes: Start from s, go one vertex away at a time until all are visited
            Base Cases:
            Logic:
        Runtime: 
        '''
        pass

    def run_dfs_helper(self, r: int, c: int, v: tuple, visited: set) -> bool:
        ROWS, COLUMNS = len(self.matrix), len(self.matrix[0])
        # If matches the v we're looking for and it's a free block
        if r == v[0] and c == v[1] and self.matrix[r][c] == 0:
            return True
        # If we reach an edge, blocked area, or visited
        if (r >= ROWS or c >= COLUMNS or 
            min(r, c) < 0 or
            self.matrix[r][c] == 1 or 
            (r,c) in visited):
            return False
        
        visited.add((r, c))

        found = (self.run_dfs_helper(r + 1, c, v, visited) or # right
                 self.run_dfs_helper(r, c + 1, v, visited) or # up
                 self.run_dfs_helper(r - 1, c, v, visited) or  # left
                 self.run_dfs_helper(r, c - 1, v, visited)) # down

        return found
    
    def run_dfs(self, s: tuple, v: tuple) -> bool:
        '''Runs DFS on the Graph object. Returns True if s reaches v, False otherwise.
        Implementation Notes: Recursively search for path starting at s.
            Base Cases: Reach an edge/blocked area/visited 
            Recursive Relation: Irrelevant
            Logic: Recursively search for path starting at s, avoiding edges, blocked, visited.
        Runtime: O(4^n)
        '''
        found = self.run_dfs_helper(s[0], s[1], v, set())
        return found

    def count_paths_helper(self, r, c, visited) -> int:
        pass

    def count_paths(self) -> int:
        '''Counts the number of paths on the Graph object from the top left to bottom right.
        Implementation Notes: Starting at (0, 0) search all paths, avoiding edges, blocked, visited
            Base Cases: Reach an edge/blocked area/visited
            Recursive Relation:
            Logic: Recursively search from (0, 0), avoiding edges, blocked, visited
        Runtime: 
        '''
        pass

    # def sort_degree(self, s: tuple) -> list[tuple]:
    #     '''Returns a list of tuples representing vertices
    #     as integers on the matrix by ascending order of the
    #     degree of the vertex in the graph from a source
    #     vertex s.
    #     Implementation Notes: 
    #         Base Cases:
    #         Logic:
    #     Runtime: 
    #     '''
    #     pass