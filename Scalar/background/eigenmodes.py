#!/usr/bin/env python
import numpy as np

def read_bubble(fName,n):
    """
    Read in data storing the time-evolution of a background bubble
    """
    return

def d2V(phi):
    return 1.  # Define second derivative of potential

def compute_eigens(dat):
    """
    Compute the instantaneous eigenvalues and eigenmodes of the background bubble configuration.
    """
    # Construct linear operator for fluctuations.
    # Requires defining Laplacian and Hessian of potential
    L2 = d2V(dat) # + derivatives
    return

def get_coefficients():
    """
    Given the eigenmodes of the system, compute the projection of a simulation with fluctuations onto them.  This is complicated by requiring the nucleation time and position.
    """
    return

if __name__ == "__main__":
    pass
