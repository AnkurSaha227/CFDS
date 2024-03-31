import numpy as np
import matplotlib.pyplot as plt

Lx, Ly = 1.0, 1.0 # Lengths
Nx, Ny = 50, 50 # Grid points (x & y)
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1) # Grid spacing (x & y)

# Boundary
T_top, T_bottom, T_left, T_right= 100.0, 0.0, 50.0, 50.0

T_initial = np.zeros((Ny, Nx)) # arbitiary Ti


T_initial[0, :] = T_top
T_initial[-1, :] = T_bottom
T_initial[:, 0] = T_left
T_initial[:, -1] = T_right

# Using FDM
T = np.copy(T_initial)
maxi = 9000
tolerance = 1e-6

for itr in range(maxi):
    T_new = np.copy(T)
    for i in range(1, Ny-1):
        for j in range(1, Nx-1):
            T_new[i, j] = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])
    if np.max(np.abs(T_new - T)) < tolerance:
        break
    T = np.copy(T_new)
    
X, Y = np.meshgrid(np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny))

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, T, cmap='hot')
plt.colorbar(label='Temperature °C)')
plt.title(f'Distribution Gradient ({itr+1} iterations)')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.grid(True)
plt.show()
