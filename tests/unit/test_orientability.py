import numpy as np
import surfacetopology as topo
from triops import shuffle_tri, reorder_tri, sort_tri, read_tri


def test_already_oriented():
    S = topo.small_mesh('torus')
    T, = topo.surface_topology(S)
    assert np.all(T.triangles == S)

def test_connected_components():
    S = topo.small_mesh('tetrahedron')
    S5 = topo.disjoint_sum(S, S, S, S, S)
    S5 = reorder_tri(S5)
    T = topo.surface_topology(S5)
    assert len(T) == 5
    for k in range(5):
        Tk = T[k].triangles-T[k].triangles.min()
        assert(np.all(sort_tri(S) == sort_tri(Tk)))

def test_nonmanifold():
    nonmanifold = np.array([[2, 0, 1], [3, 4, 2], [2, 3, 5], 
                            [2, 0, 6], [2, 5, 7]])
    S1 = topo.small_mesh('sphere')
    S2 = nonmanifold
    S3 = topo.small_mesh('tetrahedron')
    S = topo.disjoint_sum(S1, S2, S3)
    T = topo.surface_topology(S)
    assert np.all(S1 == T[2].triangles-T[2].triangles.min())
    assert np.all(S2 == T[0].triangles-T[0].triangles.min())
    assert np.all(S3 == T[1].triangles-T[1].triangles.min())

def test_fix_orientation():
    S = read_tri('mesh2d')
    T, = topo.surface_topology(S)
    assert T.oriented and T.orientable
    assert np.all(T.triangles == S)
    S = shuffle_tri(S)
    T, = topo.surface_topology(S)
    assert not T.oriented and T.orientable
    T, = topo.surface_topology(T.triangles)
    assert T.oriented and T.orientable

def test_moebius():
    S = read_tri('moebius')
    T, = topo.surface_topology(S)
    assert not T.oriented and not T.orientable

def test_klein_bottle():
    S = read_tri('klein')
    T, = topo.surface_topology(S)
    assert not T.oriented and not T.orientable

def test_projective_plane():
    S = topo.small_mesh('projplane')
    T, = topo.surface_topology(S)
    assert not T.oriented and not T.orientable

