from intro_graphs import MatrixGraph
import pytest
# Test cases
# run pytest -rP in cmd line

@pytest.fixture
def graph1():
    grid = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
    return MatrixGraph(grid)

def test_matrix_dfs(graph1):
    assert graph1.run_dfs((0, 0), (1, 2)) == True

def test_matrix_dfs_blocked(graph1):
    assert graph1.run_dfs((0, 0), (2, 3)) == False

def test_matrix_dfs_out_bounds_v(graph1):
    assert graph1.run_dfs((0, 0), (4, 4)) == False

def test_matrix_dfs_out_bounds_s(graph1):
    assert graph1.run_dfs((-1, -1), (4, 4)) == False

def test_matrix_dfs_start_blocked(graph1):
    assert graph1.run_dfs((1, 0), (1, 4)) == False