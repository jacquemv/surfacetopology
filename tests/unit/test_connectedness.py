import numpy as np
import surfacetopology as topo
from triops import reorder_tri


def test_isolated_vertices():
    S = topo.small_mesh('torus')
    n = S.max()+1
    S[S > 6] += 10
    S[S > 3] += 20
    S += 11
    T = topo.surface_topology(S)
    nb_isolated = S.max()+1 - n
    assert len(T) == nb_isolated + 1
    S2 = topo.renumber_vertices(S)
    T = topo.surface_topology(S2)
    assert len(T) == 1

def test_two_components():
    S1 = topo.small_mesh('sphere')
    S2 = topo.small_mesh('torus')
    S = topo.disjoint_sum(S1, S2)
    T = topo.surface_topology(S)
    T1, = topo.surface_topology(S1)
    T2, = topo.surface_topology(S2)
    assert len(T) == 2
    assert T[0] == T2
    assert T[1] == T1

def test_many_components():
    names = 'torus', 'sphere', 'cylinder', 'sphere', 'tetrahedron'
    meshes = [topo.small_mesh(name) for name in names]
    S = topo.disjoint_sum(*meshes)
    T = topo.surface_topology(reorder_tri(S))
    assert len(T) == len(names)

def test_many_components_nonorientable():
    names = 'moebius', 'projplane', 'kleinbottle', 'moebius'
    meshes = [topo.small_mesh(name) for name in names]
    S = topo.disjoint_sum(*meshes)
    T = topo.surface_topology(reorder_tri(S))
    assert len(T) == len(names)
