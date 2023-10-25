from adjacency_list import AdjacencyGraph
import pytest

@pytest.fixture
def graph1(): 
    '''
     A -> B -> D
     `-> C --~^
    '''
    graph = [["A", "B"],
             ["A", "C"],
             ["B", "D"],
             ["D", "C"]]
    return graph

def test_dfs_reachable(graph1):
    graph = AdjacencyGraph(graph1)
    assert graph.run_dfs("A", "D") == True
    assert graph.run_dfs("A", "C") == True
    assert graph.run_dfs("A", "B") == True

def test_dfs_unreachable(graph1):
    graph = AdjacencyGraph(graph1)
    assert graph.run_dfs("C", "B") == False
    assert graph.run_dfs("C", "A") == False
    assert graph.run_dfs("D", "A") == False

def test_bfs_reachable(graph1):
    graph = AdjacencyGraph(graph1)
    assert graph.run_bfs("A", "D") == True
    assert graph.run_bfs("A", "C") == True
    assert graph.run_bfs("A", "B") == True

def test_bfs_unreachable(graph1):
    graph = AdjacencyGraph(graph1)
    assert graph.run_bfs("C", "B") == False
    assert graph.run_bfs("C", "A") == False
    assert graph.run_bfs("D", "A") == False
