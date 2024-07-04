# PyMono: Parameter Estimation of Mono-Component Isotherms
    The pyMono package was developed to handle parameter estimation, using Particle Swarm Optimization,
    of seven Isotherm models:
    
* Langmuir
* Langmuir-Freundlich (Sips)
* Toth
* BET
* BET-Aranovich
* GAB
* Multisite Langmuir

## User Instructions
### 1 - Defining an experimental isotherm
    The creation of the experimental isotherm can be done in two separate ways:
1. Instantiation
    * An Isotherm object may be instantiated through the command:<br>
      *pyMono.Isotherm(list: p, list: q)*, providing the constructor two lists<br>
      containing the values of experimental pressure(*p*) and adsorbed quantity(*q*)
2. Loading a .csv or .xlsx file



