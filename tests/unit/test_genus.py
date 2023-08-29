import pytest
import numpy as np
import surfacetopology as topo
from triops import read_tri

def genus(S):
    T = topo.surface_topology(S)
    assert len(T) == 1
    return T[0].genus

def test_small_mesh():
    S = topo.small_mesh('hemiicosahedron')
    T, = topo.surface_topology(S)
    assert not T.orientable
    assert T.genus == 1

def test_connected_sum_orientable():
    S = topo.small_mesh('torus')
    assert genus(S) == 1
    Sn = S
    for n in range(10):
        Sn = topo.connected_sum(Sn, S)
        assert genus(Sn) == n+2

def test_connected_sum_non_orientable():
    S = topo.small_mesh('hemiicosahedron')
    assert genus(S) == 1
    Sn = S
    for n in range(10):
        Sn = topo.connected_sum(Sn, S)
        assert genus(Sn) == n+2

def test_connected_sum_exception():
    S1 = topo.small_mesh('torus')
    S2 = topo.small_mesh('cylinder')
    with pytest.raises(ValueError):
        S = topo.connected_sum(S1, S2)

def test_connected_sum_moebius():
    S1 = read_tri('moebius')
    S2 = topo.small_mesh('hemiicosahedron')
    S = topo.connected_sum(S1, S2)
    T, = topo.surface_topology(S)
    assert T.genus == 2

def test_torus_and_projplane():
    T2 = topo.small_mesh('torus')
    P2 = topo.small_mesh('projplane')
    # S1 and S2 are homeomorphic (genus 3)
    S1 = topo.connected_sum(P2, P2, P2)
    S2 = topo.connected_sum(T2, P2)
    assert topo.homeomorphic(S1, S2)

def test_klein_and_projplane():
    S1 = topo.small_mesh('torus')
    P2 = topo.small_mesh('kleinbottle')
    # S1 and S2 are homeomorphic (genus 2)
    S2 = topo.connected_sum(P2, P2)
    assert topo.homeomorphic(S1, S2)

def test_homeomorphic():
    S = topo.small_mesh('sphere')
    assert topo.homeomorphic(S, 'sphere')
    S = topo.small_mesh('torus')
    assert topo.homeomorphic(S, 'torus')

def test_homeomorphic_nonconnected():
    S1 = topo.small_mesh('sphere')
    S2 = topo.small_mesh('torus')
    S3 = topo.disjoint_sum(S1, S2)
    S4 = topo.disjoint_sum(S2, S1)
    assert topo.homeomorphic(S3, S4)


