from libcpp.vector cimport vector

cdef extern from "rirgen.h":
	cdef vector[vector[double]] computeRIR(double c, double fs, vector[vector[double]] rr, vector[double] ss, vector[double] LL, vector[double] beta_input, vector[double] orientation, int isHighPassFilter, int nDimension, int nOrder, int nSamples, char microphone_type);

