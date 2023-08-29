import numpy as np

DATADIR = '../data'

def shuffle_tri(tri):
    if len(tri) == 0:
        return tri
    I = [0]
    while np.all(I == 0): # at least one change
        I =  np.random.random(tri.shape[0]) < 0.5
    tri2 = tri.copy()
    tri2[I] = tri2[I][:, [2, 1, 0]]
    return tri2

def reorder_tri(tri):
    return tri[np.random.permutation(tri.shape[0])]

def sort_tri(tri):
    return tri[np.lexsort(tri.T[::-1], axis=0)]

def read_tri(fname):
    tri = np.fromfile(DATADIR+'/'+fname+'.tri', sep=' ')[1:]
    return tri.astype(np.int32).reshape((-1, 3))