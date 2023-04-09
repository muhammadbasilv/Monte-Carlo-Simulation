**Department of Mechanical Engineering, NIT Calicut** 

**ME3112: Metrology and Instrumentation** 

**Assignment -2021-22 (6th Semester Mechanical Engineering)** 

**Submission: On or before 17 April 2022 11.30 pm** 

**Marks:[10]** 

- Solve the following uncertainty analyses problems using Monte Carlo simulation. Use MATLAB/Python/C program to solve the problems 
- A group of **6-7** students allotted to the group can do the problem with discussion but group reporting is not acceptable.    
- All students submit individual report with theory, program, results and discussions. 
- Submit  the assignment  in  Eduserver itself with  indication of  group/student  name/roll number  

**----------------------------------------------------------------------------------------------------------------**

**Problem 1** 

ΔG∗ 

The real efficiency of a fuel cell η = .  Compute the mean, standard uncertainty and 95% coverage 

ΔH∗

interval for real efficiency of fuel cell using MCS using 2x105 trials. Plot histogram representing the resulting PDF for the real efficiency of a fuel cell estimated by Monte Carlo simulation. 



|**Input Source** |**Type** |**PDF** |**PDF Parameters** |
| - | - | - | - |
|Gibbs Free Energy ΔG |B |Uniform |Min: 236.0 kJ/mol; Max:236.4 kJ/mol |
|Enthalpy of formation ΔH |B |Uniform |Min: 283.6 kJ/mol; Max:284.8 kJ/mol |
|Ideal Voltage E I|B |Triangular |Mean :1.3995 V, Min: 1.389 V ; Max:1.410 V |
|Real Voltage E R|B |Uniform |Min: 0.6318 V ; Max:0.6825 V |
**Problem 2** 

The model to describe an experiment can be expressed as follows:   = , where *T* is the torque, *m* is the mass of the applied load (kg), *g* is the local gravity acceleration (m/s²) and *L* is the total length of the arm (m). Compute the mean, standard uncertainty and 95% coverage interval for torque using MCS using 2x105 trials.Plot histogram representing the resulting PDF for the torque developed at end of lever estimated by Monte Carlo simulation



|**Input Source** |**Type** |**PDF** |**PDF Parameters** |
| - | - | - | - |
|Mass (m) |– due to repeatability |A |Gaussian |Mean: 36.8653 kg; SD: 8.49\*10-5 kg |
||– due to certificate |B |Gaussian |Mean: 0 kg; SD: 0.00005 kg |


|Local gravity of acceleration (g) |B |Gaussian |Mean: 9.7874867 m/s2 ; SD: 0.0000002 m/s2 |
| - | - | - | :- |
|Length of the arm (L) |B |Uniform |Min: 1999.9955m; Max: 2000.005m |
**Problem 3** 

A high purity metal (Cd) is weighted and dissolved in a certain volume of liquid solvent. The proposed model for this case is shown on Equation  

1000

=![](Aspose.Words.b7de6553-7de4-4c6b-ae74-f4f252176233.001.png)

where*  is the cadmium concentration (mg/L), *m* is the mass of the high purity metal (mg), *P* is its purity and *V* is the volume of the final solution (mL). The factor 1000 is used to convert millilitre to litre. 



|**Input Source** |**Type** |**PDF** |**PDF Parameters** |
| - | - | - | - |
|Purity (P) |B |Uniform |Min: 0.9988; Max:1.000 |
|Mass (m) |B |Gaussian |Mean: 100.28  mg; SD: 0.06 mg |
|Volume (V) |– due to  filling |B |Triangular |Mean: 100.1 mL; Min: 100 mL; Max: 100.2 mL |
||– due to  repeatability |A |Gaussian |Mean: 0.2 mL; SD: 0.04 mL |
||– due to  temperature |B |Uniform |Min: -0.084 mL; Max: 0.084 mL |
**Problem 4** 

Figure will show a simple model for the measurement of Brinell hardness. This test is executed by applying a load on a sphere made of a hard material over the surface of the test sample The model used here for the Brinell hardness (HB) is represented in Equation: 

0\.204 

\= 

` `( − √ 2 − 2 )

where F is the applied load (N), D is the indenter diameter (mm) and d is the diameter of the indentation mark (mm). 

![](Aspose.Words.b7de6553-7de4-4c6b-ae74-f4f252176233.002.jpeg)

Compute the mean, standard uncertainty and 95% coverage interval for Brinell hardness using MCS using 2x105 trials.Plot histogram representing the resulting PDF for Brinell hardness estimated by Monte Carlo simulation



|**Input Source** |**Type** |**PDF** |**PDF Parameters** |
| - | - | - | - |
|Load (F) |B |Gaussian |Mean: 29400 N; SD: 294 N |
|Intender diameter (D) |B |Uniform |Min : 10 mm; Max: 10.12 mm |
|Diameter of the mark (d) |A |Gaussian |Mean: 3 mm, SD: 0.035 mm |

