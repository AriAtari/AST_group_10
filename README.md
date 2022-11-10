White Dwarf
===========

Project directory for a model of white dwarf. A full description of the project is available on D2L.

Contents
--------

0. `README.md`: this file
1. `astro_const.py`: module containing physical constants, uses `astropy`
2. `eos.py`: starter code for the equation of state
3. `test_eos.py`: unit test for the equation of state; do not modify this file
4. `eos_table.txt`: comparison data for the equation of state, used by `test_eos.py`
5. `structure.py`: starter code to integrate stellar structure equations
6. `observations.py`: module containing class for reading and storing tabulated 
    white dwarf masses, radii, and associated uncertainties.
7. `Joyce.txt`: Table 4, Joyce et al. (2018). Data for `observations.py`.

More Documentation!
--------

    *     `eos.py`
    
- def pressure(rho, mue):
    "Calculates pressure using mass density and baryon/electron ratio. "
    
    Arguments
        rho
            mass density (kg/m**3)
        mue
            baryon/electron ratio
    
    Returns
        electron degeneracy pressure (Pascal)
        
--------------------------------------------------------

- def density(p, mue):
    " calculates density using electron degeneracy pressure and baryon/electron ratio "

    Arguments
        p
            electron degeneracy pressure (Pascal)
        mue
            baryon/electron ratio
        
    Returns
        mass density (kg/m**3)
        
--------------------------------------------------------

    *     `structure.py`

- def stellar_derivatives(m,z,mue):
    " RHS of Lagrangian differential equations for radius and pressure "
    
    
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
    

- def central_values(Pc,delta_m,mue):
    "Constructs the boundary conditions at the edge of a small, constant density core of mass delta_m with central pressure P_c"
    
    Arguments
        Pc
            central pressure (units = Pascal)
        delta_m
            core mass (units = kg)
        mue
            nucleon/electron ratio
    
    Returns
        z = array([ r, p ])
            central values of radius and pressure (units =[ m, Pascal])
    


- def lengthscales(m,z,mue):
    "Computes the radial length scale H_r and the pressure length H_P"
    
    
    Arguments
        m
            current mass coordinate (units = kg)
        z (array)
           [ r, p ] (units =[ m, Pascal])
        mue
            mean electron weight
    
    Returns
        z/|dzdm| (units =[ m, Pascal ])
    

- def integrate(Pc,delta_m,eta,xi,mue,max_steps=10000):
    "Integrates the scaled stellar structure equations"
    

    Arguments
        Pc
            central pressure (units = Pascal)
        delta_m
            initial offset from center (units = kg)
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
            integration (units:[kg,m, Pascal])
    
- def pressure_guess(m,mue):
    "Computes a guess for the central pressure based on virial theorem and mass-radius relation."
     
    
    Arguments
        m
            mass of white dwarf (units are kg)
        mue
            mean electron mass
    
    Returns
        P
            guess for pressure
   

































    
    