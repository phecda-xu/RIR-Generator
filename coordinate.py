import numpy as np

def cart2sph(x,y,z):
    x_pow2 = x**2
    y_pow2 = y**2
    azimuth = np.arctan2(y,x)
    elevation = np.arctan2(z,np.sqrt(x_pow2 + y_pow2))
    r = np.sqrt(x_pow2 + y_pow2 + z**2)
    return azimuth, elevation, r

def sph2cart(azimuth,elevation,r):
    cos_elevation = np.cos(elevation)
    x = r * cos_elevation * np.cos(azimuth)
    y = r * cos_elevation * np.sin(azimuth)
    z = r * np.sin(elevation)
    return [x, y, z]