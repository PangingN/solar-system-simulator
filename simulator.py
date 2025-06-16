G = 6.67430e-11  # Gravitational constant
SUN_MASS = 1.989e30  # Mass of the Sun (kg)

# def compute_gravitational_force(mass1, mass2, distance):
#     return G * mass1 * mass2 / distance**2

def simulate_orbit(position, velocity, time_step, steps):
    trajectory = []
    for _ in range(steps):
        # Calculate distance to the Sun
        distance = (position[0]**2 + position[1]**2)**0.5
        
        # Update velocity
        velocity[0] -= (G * SUN_MASS * position[0] / distance**3) * time_step
        velocity[1] -= (G * SUN_MASS * position[1] / distance**3) * time_step
        
        # Update position
        position[0] += velocity[0] * time_step
        position[1] += velocity[1] * time_step
        
        # Save position for visualization
        trajectory.append((position[0], position[1]))
    return trajectory
