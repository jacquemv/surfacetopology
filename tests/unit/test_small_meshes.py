import numpy as np
import surfacetopology as topo


def test_sphere():
    T, = topo.surface_topology(topo.small_mesh('Sphere'))
    assert T.manifold
    assert T.oriented and T.orientable
    assert topo.surface_topology
    T.sizes == (3, 3, 2, 0)
    assert T.genus == 0

def test_tetrahedron():
    T, = topo.surface_topology(topo.small_mesh('tetrahedron'))
    assert T.manifold
    assert T.oriented and T.orientable
    assert topo.surface_topology
    T.sizes == (4, 6, 4, 0)
    assert T.genus == 0

def test_cylinder():
    T, = topo.surface_topology(topo.small_mesh('cylinder'))
    assert T.manifold
    assert T.oriented and T.orientable
    assert topo.surface_topology
    T.sizes == (6, 12, 6, 2)
    assert T.genus == 0

def test_moebius():
    T, = topo.surface_topology(topo.small_mesh('moebius'))
    assert T.manifold
    assert not T.oriented and not T.orientable
    assert topo.surface_topology
    T.sizes == (6, 12, 6, 1)
    assert T.genus == 1

def test_torus():
    T, = topo.surface_topology(topo.small_mesh('TORUS'))
    assert T.manifold
    assert T.oriented and T.orientable
    assert topo.surface_topology
    T.sizes == (7, 21, 14, 0)
    assert T.genus == 1

def test_projplane():
    T, = topo.surface_topology(topo.small_mesh('projplane'))
    assert topo.surface_topology
    T.sizes == (6, 15, 10, 0)
    assert T.manifold
    assert not T.oriented and not T.orientable
    assert T.genus == 1

def test_klein_bottle():
    T, = topo.surface_topology(topo.small_mesh('kleinbottle'))
    assert topo.surface_topology
    T.sizes == (9, 27, 18, 0)
    assert T.manifold
    assert not T.oriented and not T.orientable
    assert T.genus == 2