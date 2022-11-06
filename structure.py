########################################################################
# Team Spectacular Stellars: Arian Andalib, Ashley Stone, Jonathan Kho, Emma Oswald
# AST 304, Fall 2022
# Michigan State University
########################################################################
"""
<Description of this module goes here: what it does, how it's used.>
"""

import numpy as np
from eos import * # fill this in
from ode import rk4 # fill this in
from astro_const import * # fill this in

def stellar_derivatives(m,z,mue):
    """
    RHS of Lagrangian differential equations for radius and pressure
    
    Arguments
        m
            current value of the mass
        z (array)
            current values of (radius, pressure)
        mue
            ratio, nucleons to electrons.  For a carbon-oxygen white dwarf, 
            mue = 2.
        
    Returns
        dzdm (array)
            Lagrangian derivatives dr/dm, dP/dm
    """
    
    rho = density(z[1], mue)
    
    dzdm = np.zeros_like(z)

    # evaluate dzdm
    drdm = (4*np.pi*z[0]**2*rho)**(-1)
    dPdm = (-G*m)/(4*np.pi*z[0]**4)
    
    dzdm = np.array([drdm, dPdm])
    
    return dzdm

def central_values(Pc,delta_m,mue):
    """
    Constructs the boundary conditions at the edge of a small, constant density 
    core of mass delta_m with central pressure P_c
    
    Arguments
        Pc
            central pressure (units = ?)
        delta_m
            core mass (units = ?)
        mue
            nucleon/electron ratio
    
    Returns
        z = array([ r, p ])
            central values of radius and pressure (units = ?)
    """
    
    # compute initial values of z = [ r, p ]
    
    m = delta_m
    
    P = Pc
    rho = density(P, mue)
    r = ((3*m)/(4*np.pi*rho))**(1/3)
    
    z = [r, P]
    
    return z
    
def lengthscales(m,z,mue):
    """
    Computes the radial length scale H_r and the pressure length H_P
    
    Arguments
        m
            current mass coordinate (units = ?)
        z (array)
           [ r, p ] (units = ?)
        mue
            mean electron weight
    
    Returns
        z/|dzdm| (units = ?)
    """

    # fill this in
    
    Hr = 4*np.pi*z[0]**3*density(z[1],mue)
    
    Hp = 4*np.pi*z[0]**4*z[1]/(G*m)
    
    return np.array([Hr,Hp])
    
def integrate(Pc,delta_m,eta,xi,mue,max_steps=10000):
    """
    Integrates the scaled stellar structure equations

    Arguments
        Pc
            central pressure (units = ?)
        delta_m
            initial offset from center (units = ?)
        eta
            The integration stops when P < eta * Pc
        xi
            The stepsize is set to be xi*min(p/|dp/dm|, r/|dr/dm|)
        mue
            mean electron mass
        max_steps
            solver will quit and throw error if this more than max_steps are 
            required (default is 10000)
                        
    Returns
        m_step, r_step, p_step
            arrays containing mass coordinates, radii and pressures during 
            integration (what are the units?)
    """
        
    m_step = np.zeros(max_steps)
    r_step = np.zeros(max_steps)
    p_step = np.zeros(max_steps)
    
    # set starting conditions using central values
    m = delta_m
    z = central_values(Pc,delta_m,mue)
    Nsteps = 0
    for step in range(max_steps):
        radius = z[0]
        pressure = z[1]
        
        # are we at the surface?
        if (pressure < eta*Pc):
            break
            
        # store the step
        m_step[step] = m
        r_step[step] = z[0]
        p_step[step] = z[1]
        
        # set the stepsize
        h = xi*min(lengthscales(m,z,mue))
        
        # take a step
        z = rk4(stellar_derivatives,m,z,h,mue)
        m += h
        
        # increment the counter
        Nsteps += 1
        
    # if the loop runs to max_steps, then signal an error
    else:
        raise Exception('too many iterations')
        
    return m_step[0:Nsteps],r_step[0:Nsteps],p_step[0:Nsteps]

def pressure_guess(m,mue):
    """
    Computes a guess for the central pressure based on virial theorem and mass-
    radius relation. 
    
    Arguments
        m
            mass of white dwarf (units are ?)
        mue
            mean electron mass
    
    Returns
        P
            guess for pressure
    """
    # fill this in
    
    # For optional calibration
    # alpha = 
    # beta = 
    # Pguess = (alpha**5/beta**(20/3))*(G**5/Ke**4)*(m*mue**2)**(10/3)
    
    Pguess = (1/40.09269)*(G**5/Ke**4)*(m*mue**2)**(10/3)
    
    return Pguess
