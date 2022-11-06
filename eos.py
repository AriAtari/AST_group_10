########################################################################
# Team Spectacular Stellars: Arian Andalib, Ashley Stone, Jonathan Kho, Emma Oswald
# AST 304, Fall 2022
# Michigan State University
########################################################################
"""
<Description of this module goes here: what it does, how it's used.>
"""

import astro_const as ac
import numpy as np

def pressure(rho, mue):
    """
    Arguments
        rho
            mass density (kg/m**3)
        mue
            baryon/electron ratio
    
    Returns
        electron degeneracy pressure (Pascal)
    """
    
    # replace following lines with body of routine
    p = (1/5)*(3/(8*(np.pi)))**(2/3)*(ac.h**2/ac.m_e)*(rho/(mue*ac.m_u))**(5/3)
    return p

def density(p, mue):
    """
    Arguments
        p
            electron degeneracy pressure (Pascal)
        mue
            baryon/electron ratio
        
    Returns
        mass density (kg/m**3)
    """
    
    # replace following lines with body of routine
    rho = ((p/((1/5)*(3/(8*(np.pi)))**(2/3)*(ac.h**2/ac.m_e)))**(3/5))*(mue*ac.m_u)
    return rho
