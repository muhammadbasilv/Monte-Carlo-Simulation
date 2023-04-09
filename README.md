#Monte Carlo Simulation
**Problem Statement** 


The real efficiency of a fuel cell η =  (ΔG∗Er) / (ΔH*Ei).  Compute the mean, standard uncertainty and 95% coverage interval for real efficiency of fuel cell using MCS using 2x105 trials. Plot histogram representing the resulting PDF for the real efficiency of a fuel cell estimated by Monte Carlo simulation. 



|**Input Source** |**Type** |**PDF** |**PDF Parameters** |
| - | - | - | - |
|Gibbs Free Energy ΔG |B |Uniform |Min: 236.0 kJ/mol; Max:236.4 kJ/mol |
|Enthalpy of formation ΔH |B |Uniform |Min: 283.6 kJ/mol; Max:284.8 kJ/mol |
|Ideal Voltage E I|B |Triangular |Mean :1.3995 V, Min: 1.389 V ; Max:1.410 V |
|Real Voltage E R|B |Uniform |Min: 0.6318 V ; Max:0.6825 V |

