import numpy as np
import surfacetopology as topo
from triops import shuffle_tri


def test_nonmanifold_vertex1():
    T, = topo.surface_topology([[0, 1, 2], [0, 4, 3]])
    assert not T.manifold
    assert np.all(T.nonmanifold_vertices == [0])

def test_nonmanifold_vertex2():
    T, = topo.surface_topology([[2, 0, 1], [3, 4, 2], [2, 3, 5]])
    assert not T.manifold
    assert np.all(T.nonmanifold_vertices == [2])

def test_nonmanifold_vertex3():
    T, = topo.surface_topology([[2, 0, 1], [3, 4, 2], [2, 3, 5], 
                           [2, 0, 6], [2, 5, 7]])
    assert not T.manifold
    assert np.all(T.nonmanifold_vertices == [2])

def test_nonmanifold_vertex4():
    n = 100
    S = np.row_stack((np.zeros(n), np.arange(n)+1, np.arange(n)+2)).T
    T, = topo.surface_topology(shuffle_tri(S.astype(int)))
    assert T.manifold 

def test_nonmanifold_vertex5():
    S = topo.small_mesh('torus')
    S = shuffle_tri(np.delete(S, [6, 8], 0))
    T, = topo.surface_topology(S)
    assert not T.manifold
    assert np.all(T.nonmanifold_vertices == [0])