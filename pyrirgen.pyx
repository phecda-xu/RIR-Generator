cimport cdefs
import collections

def rir_generator(soundVelocity, fs, sourcePosition, receiverPositions, roomMeasures, *, reverbTime=None, betaCoeffs=None, orientation=[.0, .0], bint isHighPassFilter=True, int nDim=3, int nOrder=-1, int nSamples=-1, micType='o'):
	""" Computes the response of an acoustic source to one or more microphones in a reverberant room using the image method [1,2].

	Room Impulse Response Generator

	Computes the response of an acoustic source to one or more
	microphones in a reverberant room using the image method [1,2].

	Author    : dr.ir. Emanuel Habets (ehabets@dereverberation.org)

	Version   : 2.1.20141124

	Copyright (C) 2003-2014 E.A.P. Habets, The Netherlands.

	[1] J.B. Allen and D.A. Berkley,
		Image method for efficiently simulating small-room acoustics,
		Journal Acoustic Society of America,
		65(4), April 1979, p 943.

	[2] P.M. Peterson,
		Simulating the response of multiple microphones to a single
		acoustic source in a reverberant room, Journal Acoustic
		Society of America, 80(5), November 1986.

	Args:
		c (float): sound velocity in m/s
		fs (float): sampling frequency in Hz
		receiverPositions (list[list[float]]): M x 3 array specifying the (x,y,z) coordinates of the receiver(s) in m
		sourcePosition (list[float]): 1 x 3 vector specifying the (x,y,z) coordinates of the source in m
		roomMeasures (list[float]): 1 x 3 vector specifying the room dimensions (x,y,z) in m
		betaCoeffs (list[float]): 1 x 6 vector specifying the reflection coefficients [beta_x1 beta_x2 beta_y1 beta_y2 beta_z1 beta_z2]
		reverbTime (float): reverberation time (T_60) in seconds
		nSample (int): number of samples to calculate, default is T_60*fs
		micType (str): [omnidirectional, subcardioid, cardioid, hypercardioid, bidirectional], default is omnidirectional
		nOrder (int): reflection order, default is -1, i.e. maximum order
		nDim (int): room dimension (2 or 3), default is 3
		orientation (list[float]): direction in which the microphones are pointed, specified using azimuth and elevation angles (in radians), default is [0 0]
		isHighPassFilter (bool)^: use 'False' to disable high-pass filter, the high-pass filter is enabled by default.

	Return:
		list[list[float]]: M x nsample matrix containing the calculated room impulse response(s)
	"""
	if not (reverbTime is None) != (betaCoeffs is None):
		raise ValueError('You provide either reverbTime or betaCoeffs.')
	if betaCoeffs is None:
		betaCoeffs = [reverbTime]

	"""Number of samples: Default T60 * Fs"""
	if 'nSamples' == -1:
		nSamples=int(reverbTime * fs)

	if all(isinstance(e, collections.Iterable) for e in receiverPositions):
		multipleMics = True
	else:
		multipleMics = False
		receiverPositions = [receiverPositions]

	h = cdefs.computeRIR(soundVelocity, fs, receiverPositions, sourcePosition, roomMeasures, betaCoeffs, orientation, isHighPassFilter, nDim, nOrder, nSamples, ord(micType[0]))

	if multipleMics:
		return h
	return h[0]
