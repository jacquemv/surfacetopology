import surfacetopology as topo

S1 = topo.small_mesh('tetrahedron')
S1
topo.surface_topology(S1)

S2 = topo.small_mesh('torus')
S = topo.disjoint_sum(S1, S2, 10+S1)
len(topo.surface_topology(S))
S = topo.renumber_vertices(S)
len(topo.surface_topology(S))

S3 = topo.small_mesh('moebius')
topo.surface_topology(S3)

S = topo.connected_sum(S2, S2, S2)
topo.surface_topology(S)