import numpy as np
import matplotlib.pyplot as plt

'''
PSEUDOCODE

Import necessary libraries (numpy and matplotlib)
 
Initialize parameters:
Grid size = 100x100
Infection probability = 0.3
Recovery probability = 0.05
Number of time steps = 100
Save time points = [0, 10, 50, 100]
Initialize a 100x100 grid, all elements set to 0 (susceptible individuals)
 
Randomly select an initial infection point, set this point to 1 (infected individual)
 
For each time step from 0 to the number of time steps:
Step 1: Handle recovery
Find the positions of all infected individuals
For each infected individual, decide whether to recover based on the recovery probability
Set recovered individuals to 2 (recovered individuals)
 
Step 2: Handle new infections
Initialize an empty list to store the positions of new infections
For each current infected individual, check their 8 neighbors
If the neighbor is within the grid boundaries and is susceptible, decide whether to infect based on the infection probability
If infected, add the neighbor's position to the new infection list
Batch update the positions of new infections to infected (avoid duplicate infections)
 
Step 3: Save images at specified time points
If the current time step is in the list of save time points:
Create a new image
Display the current grid state
Save the image as a file
 
After the simulation is complete, print the completion information and the filenames of the saved images
'''

# Initialize Grid

GRID_SIZE = 100      # Grid size (100x100)
BETA = 0.3           # Infection probability
GAMMA = 0.05         # Recovery probability
TIME_STEPS = 100     # Time steps
SAVE_TIMES = [0, 10, 50, 100]  # Time points
population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)  # 0=Susceptible, 1=Infected, 2=Recovered

# Randomly select coordinates for the initial infected individual
outbreak = np.random.choice(GRID_SIZE, size=2)
population[outbreak[0], outbreak[1]] = 1

for t in range(TIME_STEPS + 1):
    # Step 1: Handle infected individuals recovering
    # Find coordinates of all infected individuals
    infected_coords = np.argwhere(population == 1)
    recovery_mask = np.random.rand(len(infected_coords)) < GAMMA
    # Convert eligible infected individuals to recovered
    for idx in infected_coords[recovery_mask]:
        population[tuple(idx)] = 2
    # Step 2: Handle new infections
    new_infections = []
    # Iterate through all currently infected individuals
    for (i, j) in infected_coords: # Check 8 neighbors
        for di in [-1, 0, 1]: 
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # Skip self
                ni, nj = i + di, j + dj
                if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE: # Check boundaries
                    if population[ni, nj] == 0 and np.random.rand() < BETA:
                        new_infections.append((ni, nj)) # Only infect susceptible individuals
    
    # Batch update new infections (avoiding duplicate infections)
    for (ni, nj) in new_infections:
        if population[ni, nj] == 0:
            population[ni, nj] = 1

    # Step 3: Save images at key time points
    if t in SAVE_TIMES:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(
            population,
            cmap='viridis',    # Color map
            interpolation='nearest'
        )
        plt.title(f'2D SIR Model (t={t})')
        plt.axis('off')
        plt.savefig(f'spatial_SIR_t{t}.png')
        #plt.close()

print("Simulation complete!")
print(f"--> spatial_SIR_t{SAVE_TIMES}.png")