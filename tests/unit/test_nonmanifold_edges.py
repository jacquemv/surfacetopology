import numpy as np
import surfacetopology as topo


def test_nonmanifold_edge1():
    T, = topo.surface_topology([[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5]])
    assert not T.manifold
    assert np.all(T.nonmanifold_edges == [[0, 1]])

def test_nonmanifold_edge2():
    T, = topo.surface_topology([[0, 1, 2], [0, 1, 3], [0, 1, 4], 
                                [2, 1, 5], [2, 1, 6]])
    assert not T.manifold
    assert np.all(T.nonmanifold_edges == [[0, 1], [1, 2]])

def test_nonmanifold_edge3():
    T, = topo.surface_topology([[0, 1, 2], [0, 1, 3], [0, 1, 4], 
                                [2, 1, 5], [2, 1, 6],
                                [2, 0, 7], [0, 2, 8]])
    assert not T.manifold
    assert np.all(T.nonmanifold_edges == [[0, 1], [1, 2], [2, 0]])

def test_nonmanifold_edge4():
    S = topo.small_mesh('torus')
    S = np.row_stack((S, [S[4, 0], S[4, 2], S.max()+1]))
    T, = topo.surface_topology(S)
    assert not T.manifold
    assert np.all(T.nonmanifold_edges == [[S[4, 0], S[4, 2]]])