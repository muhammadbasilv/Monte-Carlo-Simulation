import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (8.5,6.5)

"""$$\eta_R = \dfrac{ΔG ⋅ E_R}{ΔH ⋅ E_I},$$ where:
$$ η_R : \text{Real Efficiency of fuel cell} \\
ΔG : \text{Gibbs Free Energy} \\
ΔH : \text{Enthalpy of Formation} \\
E_I : \text{Ideal Voltage} \\
E_R : \text{Real Voltage}$$
"""

N = 200000 #sampling size

PDF_dG = np.random.uniform(236.0,236.4,N) #Uniform distribution for Delta G
plt.hist(PDF_dG,bins = np.linspace(235.9,236.5,181))
plt.title(r"$\Delta G\; vs\; frequency$")
plt.xlabel(r'$\Delta G\;{(kJ/mol)}^{-1}$')
plt.ylabel(r'$frequency$')
plt.show()
print(f"Delta G is a uniform distribution with mean:{PDF_dG.mean()} kJ/mol \\
    and standard uncertainity:{PDF_dG.std()} kJ/mol")

PDF_dH = np.random.uniform(283.6,284.8,N) #Uniform distribution for Delta H
plt.hist(PDF_dH,bins = np.linspace(283.4,285.0,181))
plt.title(r"$\Delta H\; vs\; frequency$")
plt.xlabel(r'$\Delta H\;{(kJ/mol)}^{-1}$')
plt.ylabel(r'$frequency$')
plt.show()
print(f"Delta H is a uniform distribution with mean:{PDF_dH.mean()} kJ/mol \\
    and standard uncertainity:{PDF_dH.std()} kJ/mol")

PDF_Ei = np.random.triangular(1.389,1.3995,1.410,N) #Triangular distribution \\
for E_i
plt.hist(PDF_Ei,bins = np.linspace(1.386,1.413,181))
plt.title(r"$E_i\; vs\; frequency$")
plt.xlabel(r'$E_i\; {V}^{-1}$')
plt.ylabel(r'$frequency$')
plt.show()
print(f"Ei is a triangular distribution with mean:{PDF_Ei.mean()} V and \\
    standard uncertainity:{PDF_Ei.std()} V")

PDF_Er = np.random.uniform(0.6318,0.6825,N) #Uniform distribution for E_r
plt.hist(PDF_Er,bins = np.linspace(0.6314,0.6824,181))
plt.title(r"$E_r\; vs\; frequency$")
plt.xlabel(r'$E_r\; {V}^{-1}$')
plt.ylabel(r'$frequency$')
plt.show()
print(f"Er is a uniform distribution with mean:{PDF_Er.mean()} V and \\
    standard uncertainity:{PDF_Er.std()} V")

PDF_Nr = PDF_dG*PDF_Er/(PDF_dH*PDF_Ei)
plt.hist(PDF_Nr,bins = np.linspace(0.3719,0.4088,2000))
plt.title(r"$Real\;efficiency,\eta_R\; vs\; frequency$")
plt.xlabel(r'$Real\;efficiency,\eta_R$')
plt.ylabel(r'$frequency$')

print(f'The resultant distribution of real efficiency has a mean of \\
    {PDF_Nr.mean()} and standard uncertainity of {PDF_Nr.std()}')
PDF_Nr.sort()
ll = int(((2.5/100)*N)-1) #lower limit
ul = int(N - ((2.5/100)*N) - 1) #upper limit
print(f"The coverage interval for 95% confidence is ({PDF_Nr[ll]}, \\
    {PDF_Nr[ul]})")


plt.axvline(x=PDF_Nr[ll],color = 'r')
plt.axvline(x=PDF_Nr[ul],color = 'r')
plt.show()

