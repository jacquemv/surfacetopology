import numpy as np
import surfacetopology as topo
from triops import shuffle_tri, read_tri, DATADIR


def test_1triangles():
    T, = topo.surface_topology([[2, 0, 1]])
    assert T.n_boundaries == 1
    assert np.all(T.boundaries[0] == [1, 0, 2])

def test_3triangles():
    T, = topo.surface_topology([[0, 1, 2], [2, 1, 3], [1, 0, 4]])
    assert T.n_boundaries == 1
    assert np.all(T.boundaries[0] == [4, 0, 2, 3, 1])

def test_cylinder():
    T, = topo.surface_topology(topo.small_mesh('cylinder'))
    assert T.n_boundaries == 2
    assert np.all(T.boundaries[1] == [4, 1, 5])
    assert np.all(T.boundaries[0] == [3, 0, 2])

def test_torus():
    T, = topo.surface_topology(topo.small_mesh('torus'))
    assert T.n_boundaries == 0

def test_small_moebius():
    T, = topo.surface_topology(topo.small_mesh('moebius'))
    assert T.n_boundaries == 1
    assert np.all(T.boundaries[0] == [4, 1, 3, 2, 0, 5])

def test_large_moebius():
    T, = topo.surface_topology(read_tri('moebius'))
    assert T.n_boundaries == 1

def test_atria_boundaries_oriented():
    for k in 1, 2, 3, 4:
        with open(DATADIR+f'/leftatrium{k}.bound', 'rt') as file:
            lines = file.readlines()
        S = read_tri(f'leftatrium{k}')
        T, = topo.surface_topology(S)
        assert T.manifold
        assert len(lines) == T.n_boundaries
        assert T.genus == (k == 3)
        for line in lines:
            B = np.fromstring(line, dtype=int, sep=' ')[:-1]
            for b in T.boundaries:
                if B[0] in b:
                    assert len(B) == len(b)
                    i = np.where(B[0] == b)[0][0]
                    assert np.all(B == np.roll(b, -i))

def test_atria_boundaries_nonoriented():
    for k in 1, 2, 3, 4:
        with open(DATADIR+f'/leftatrium{k}.bound', 'rt') as file:
            lines = file.readlines()
        S = read_tri(f'leftatrium{k}')
        T, = topo.surface_topology(shuffle_tri(S))
        assert T.manifold
        assert len(lines) == T.n_boundaries
        assert T.genus == (k == 3)
        for line in lines:
            B = np.fromstring(line, dtype=int, sep=' ')[:-1]
            for b in T.boundaries:
                if B[0] in b:
                    assert len(B) == len(b)
                    b2 = b[::-1]
                    i = np.where(B[0] == b)[0][0]
                    i2 = np.where(B[0] == b2)[0][0]
                    assert (np.all(B == np.roll(b, -i)) # either orientation
                            or np.all(B == np.roll(b2, -i2)))

