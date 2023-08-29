all:
	g++ -DBENCH debug.cpp -I../../surfacetopology -o topology
	time ./topology ../data/finemesh2d.tri

bench:
	g++ debug.cpp -o topology -I../../surfacetopology -pg -fno-pie -fno-builtin
	./topology ../data/finemesh2d.tri
	gprof ./topology > profile.txt
	rm gmon.out
	grep TriSurfTopology profile.txt | less

clean:
	rm -f ./topology profile.txt
