
CXXFLAGS = -fPIC -Wall -Wextra -c -O3
LDFLAGS = -shared

pyrirgen.so: librirgen.so
	python3 setup.py build_ext --inplace

librirgen.so: rirgen.o
	$(CXX) $(LDFLAGS) -o librirgen.so rirgen.o

rirgen.o: rirgen.cpp
	$(CXX) $(CXXFLAGS) -std=c++11 rirgen.cpp

clean:
	rm -f librirgen.o
	rm -f librirgen.so
	rm -r pyrirgen.*.so
