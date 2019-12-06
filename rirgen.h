#include <vector>

std::vector< std::vector<double> > gen_rir(double c, double fs, const std::vector< std::vector<double> >& rr, const std::vector<double>& ss, const std::vector<double>& LL, const std::vector<double>& beta_input, const std::vector<double>& orientation, int isHighPassFilter=1, int nDimension=3, int nOrder=-1, int nSamples=-1, char microphone_type='o');
