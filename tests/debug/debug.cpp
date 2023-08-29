#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include "trisurftopology.cpp"


int* read_tri(const char* fname, int& nt_tot)
{
    std::ifstream file(fname);
    file >> nt_tot;
    int* tri = new int [3*nt_tot];
    for (int i=0;i<3*nt_tot;i++) file >> tri[i];
    file.close();
    return tri;
}

void print_vector(std::vector<int> v)
{
    std::cout << "(" << v.size() << ") ";
    for (int i=0;i<v.size();i++) {
        std::cout << v[i] << " ";
    }
}

int main(int argc, char* argv[])
{
    int nt;
    int* tri = read_tri(argv[1], nt);
    TriSurfTopology topo(nt, tri);
    topo.determine_topology();
    printf("\n");
    std::cout << "nv_tot = " << topo.nv_tot << ", nt_tot = " << topo.nt_tot 
              << ", ne_tot = " << topo.ne_tot << "\n";
    std::cout << "ncomp = " << topo.ncomp << "\n";
    //for (int i=0;i<topo.nv_tot;i++) std::cout << topo.comp.label[i] << " "; std::cout << "\n";
    for (int c=0;c<topo.ncomp;c++) {
        std::cout << "  comp " << c << ": nver = " << topo.nv[c] 
                  << ", ntri = " << topo.nt[c]
                  << ", nedges = " << topo.ne[c] 
                  << ", nbound = " << topo.nbound[c] 
                  << "\n  oriented = " << topo.oriented[c] 
                  << ", orientable = " << topo.orientable[c] 
                  << ", manifold = " << topo.manifold[c] 
                  << "\n";
        printf("    nonmanifold vertices: ");
        print_vector(topo.nonmanifold_vertices[c]);
        std::cout << "\n";
        printf("    nonmanifold edges: ");
        print_vector(topo.nonmanifold_edges[c]);
        std::cout << "\n";
        printf("    collapsed triangles: ");
        print_vector(topo.collapsed_triangles[c]);
        std::cout << "\n";
    }
    printf("\n");

    HalfEdgeMap edgemap;
    edgemap.allocate(topo.nv_tot, nt, tri);

    // for (int i=0;i<topo.nt_tot;i++) {
    //     fprintf(stderr, "%d %d %d\n", topo.adjtri[3*i], topo.adjtri[3*i+1], topo.adjtri[3*i+2]);
    // }
}