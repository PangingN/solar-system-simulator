# solar-system-simulator
# STARTING WITH ONE PLANET

import plotly.graph_objects as go
# import numpy as np

# mathematical process:
# gravitational force equation -> GmM/r^2
# F = ma = GMm/r^2
# a = v/time_step = GM/r^2
# v = GM/r^2 * time_step
# components of velocity:
# v(vertical) = GM/r^2 * (sintheta) = GM/r^2 * x/r
# v(horizontal) = GM/r^2 * (costheta) = GM/r^2 * y/r

def simulate_orbit_animation(mass, position, velocity, time_step, steps): #Keeping mass so I cna use this for multiple planets where mass planet actually matters
    trajectory = []  # Store all positions for animation
    for whatever in range(steps):
        distance = (position[0]**2 + position[1]**2)**0.5 #radius
        # Update velocity in components using gravitational force
        velocity[0] -= (G * SUN_MASS * position[0] / distance**3) * time_step
        velocity[1] -= (G * SUN_MASS * position[1] / distance**3) * time_step
        # Update position in components
        position[0] += velocity[0] * time_step
        position[1] += velocity[1] * time_step
        # Save position at each step as a list of tuples 
        trajectory.append((position[0], position[1]))
    return trajectory

# Constants
G = 6.67430e-11  # Gravitational constant
SUN_MASS = 1.989e30  # Mass of the Sun
planet_mass = 5.972e24  # Earth's mass
initial_position = [1.496e11, 0]  # 1 AU from Sun
initial_velocity = [0, 29.78e3]  # Earth's orbital velocity
time_step = 60 * 60  # 1 hour
steps = 500  # Simulation steps

# Get trajectory data
trajectory = simulate_orbit_animation(planet_mass, initial_position, initial_velocity, time_step, steps)
x_coords, y_coords = zip(*trajectory) # seperates the x and y positions into lists

# Create animation frames
frames = []
for i in range(len(x_coords)):
    frames.append(go.Frame(data=[
        go.Scatter(x=x_coords[:i+1], y=y_coords[:i+1], mode='lines', name='Orbit'), #traces orbit like
        go.Scatter(x=[x_coords[i]], y=[y_coords[i]], mode='markers', marker=dict(size=10, color='blue'), name='Planet'), #shows planet at a given time
        go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=15, color='yellow'), name='Sun') #ok not really needed but gives an intial staring point
    ]))

# Create figure with initial frame
fig = go.Figure(
    data=[
        go.Scatter(x=[], y=[], mode='lines', name='Orbit'),
        go.Scatter(x=[], y=[], mode='markers', marker=dict(size=10, color='blue'), name='Planet'),
        go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=15, color='yellow'), name='Sun')
    ],
    frames=frames
)

# Layout for animation
fig.update_layout(
    title="Orbital Simulation",
    xaxis=dict(range=[-2e11, 2e11]), #domain of graph
    yaxis=dict(range=[-2e11, 2e11]),
    updatemenus=[{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }]
)

fig.show()


# NEWER CODE THAT DOESN'T WORK EITHER
# import plotly.graph_objects as go

# # Simulate orbital data
# def simulate_orbit_animation(mass, position, velocity, time_step, steps):
#     trajectory = []  # Store all positions for animation
#     for _ in range(steps):
#         distance = max((position[0]**2 + position[1]**2)**0.5, 1e-10)
#         # Update velocity using gravitational force
#         velocity[0] -= (G * SUN_MASS * position[0] / distance**3) * time_step
#         velocity[1] -= (G * SUN_MASS * position[1] / distance**3) * time_step
#         # Update position
#         position[0] += velocity[0] * time_step
#         position[1] += velocity[1] * time_step
#         # Save position at each step
#         trajectory.append((position[0], position[1]))
#     return trajectory

# # Constants
# G = 6.67430e-11  # Gravitational constant
# SUN_MASS = 1.989e30  # Mass of the Sun
# planet_mass = 5.972e24  # Earth's mass
# initial_position = [1.496e11, 0]  # 1 AU from Sun
# initial_velocity = [0, 29.78e3]  # Earth's orbital velocity

# orbital_period = 365.25 * 24 * 60 * 60  # Seconds in one Earth year
# time_step = 1 * 60  # 1 minute in seconds
# steps = int(orbital_period / time_step)  # Total steps for a full orbit

# # Get trajectory data
# trajectory = simulate_orbit_animation(planet_mass, initial_position, initial_velocity, time_step, steps)
# x_coords, y_coords = zip(*trajectory)

# # Create animation frames
# frames = []
# frame_skip = 10
# for i in range(0, len(x_coords), frame_skip):  # Apply frame skipping
#     frames.append(go.Frame(data=[
#         go.Scatter(x=x_coords[:i+1], y=y_coords[:i+1], mode='lines', name='Orbit'),
#         go.Scatter(x=[x_coords[i]], y=[y_coords[i]], mode='markers', marker=dict(size=10, color='blue'), name='Planet'),
#         go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=15, color='yellow'), name='Sun')
#     ]))

# # Create figure with initial frame
# fig = go.Figure(
#     data=[
#         go.Scatter(x=[], y=[], mode='lines', name='Orbit'),
#         go.Scatter(x=[], y=[], mode='markers', marker=dict(size=10, color='blue'), name='Planet'),
#         go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=15, color='yellow'), name='Sun')
#     ],
#     frames=frames
# )

# # Layout for animation
# fig.update_layout(
#     title="Simple Orbital Sim",
#     xaxis=dict(range=[-3e11, 3e11]),
#     yaxis=dict(range=[-3e11, 3e11]),
#     updatemenus=[{
#         "buttons": [
#             {
#                 "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],  # Adjusted duration
#                 "label": "Play",
#                 "method": "animate"
#             },
#             {
#                 "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
#                 "label": "Pause",
#                 "method": "animate"
#             }
#         ],
#         "direction": "left",
#         "pad": {"r": 10, "t": 87},
#         "showactive": False,
#         "type": "buttons",
#         "x": 0.1,
#         "xanchor": "right",
#         "y": 0,
#         "yanchor": "top"
#     }]
# )

# fig.show()
