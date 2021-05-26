import numpy as np

def rp_peaks(xx,yy):
    zz = 3*(1-xx)**2*np.exp(-(xx**2) - (yy+1)**2) - 10*(xx/5 - xx**3 - yy**5)*np.exp(-xx**2-yy**2) - 1/3*np.exp(-(xx+1)**2 - yy**2)
    return zz

def rp_peak_dataset_create(dx):
    x = np.arange(start=-3,stop=-3,step=dx)
    xx,yy = np.meshgrid(x,x)

    zz = rp_peaks(xx,yy)

    x_out = xx.flatten()
    y_out = yy.flatten()
    z_out = zz.flatten()