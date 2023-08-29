import numpy as np
import surfacetopology as topo


def test_collapsed_to_single_point1():
    T, = topo.surface_topology([[0, 0, 0]])
    assert not T.manifold

def test_collapsed_to_single_point2():
    T, = topo.surface_topology([[1, 1, 1], [0, 1, 2]])
    assert not T.manifold
    assert np.all(T.collapsed_triangles == [0])
    assert np.all(T.nonmanifold_edges == [1, 1])

def test_collapsed_edges1():
    T, = topo.surface_topology([[1, 0, 1], [0, 2, 3]])
    assert not T.manifold
    assert np.all(T.collapsed_triangles == [0])

def test_collapsed_edges2():
    T, = topo.surface_topology([[0, 1, 2], [0, 1, 1]])
    assert not T.manifold
    assert np.all(T.collapsed_triangles == [1])
    assert np.all(T.nonmanifold_edges == [0, 1])
