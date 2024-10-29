import mpmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the precision for mpmath
mpmath.mp.dps = 1000  # You can adjust this value for higher N

def compute_pi_digits(N):
    """
    Computes the first N digits of π after the decimal point.
    """
    pi_str = str(mpmath.mp.pi)[2:]  # Get digits after the decimal point
    return pi_str[:N]

def compute_rep_strand_length(pi_digits, L):
    """
    Computes the rep-strand-length R(N, L) for given π digits and strand length L.
    """
    N = len(pi_digits)
    T = N - L + 1  # Total possible substrings
    substrings = [pi_digits[i:i+L] for i in range(T)]
    unique_substrings = set(substrings)
    U = len(unique_substrings)
    R = T - U  # Number of repetitions
    return R

# Define ranges for N and L
N_values = np.arange(100, 100001, 100)  # From 100 to 1000 digits
L_values = np.arange(1, 11, 1)        # Strand lengths from 1 to 10

# Prepare meshgrid for plotting
N_mesh, L_mesh = np.meshgrid(N_values, L_values)
R_mesh = np.zeros_like(N_mesh, dtype=float)

# Compute R(N, L) for each combination of N and L
for i in range(len(L_values)):
    L = L_values[i]
    for j in range(len(N_values)):
        N = N_values[j]
        pi_digits = compute_pi_digits(N)
        R = compute_rep_strand_length(pi_digits, L)
        R_mesh[i, j] = R

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(N_mesh, L_mesh, R_mesh, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('Number of Digits N')
ax.set_ylabel('Strand Length L')
ax.set_zlabel('Rep-Strand-Length R(N, L)')
ax.set_title('3D Plot of Rep-Strand-Length R(N, L)')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()


