import numpy as np
import pytest
import surfacetopology as topo

def test_empty():
    T = topo.surface_topology([[]])
    assert len(T) == 0

def test_list():
    T = topo.surface_topology([[0, 1, 2]])
    assert len(T) == 1

def test_ndarray():
    T = topo.surface_topology(np.array([[0, 1, 2]]))
    assert len(T) == 1

def test_ndarray64():
    T = topo.surface_topology(np.array([[0, 1, 2]], dtype=np.int64))
    assert len(T) == 1

def test_noncontiguous():
    S = np.array([[0, 1, 2], [0, 2, 3]])[:, ::-1]
    assert not S.data.c_contiguous
    T = topo.surface_topology(S)
    assert len(T) == 1

def test_wrong_dimension():
    with pytest.raises(ValueError):
        topo.surface_topology([1, 2, 3])

def test_wrong_shape():
    with pytest.raises(ValueError):
        topo.surface_topology([[1, 2], [3, 4]])