# NaturalSelectionSim

Natural selection simulation written in Python.

## About

NaturalSelectionSim is an experimental project that simulates evolutionary processes based on natural selection.

![NaturalSelectionSim Demo](docs/demo.gif)

The long-term goal is to create a dynamic ecosystem where creatures evolve through interactions with the environment, inherited traits, mutations, and natural selection.

## Status

Early prototype.

Currently implemented:

- ECS-based architecture
- Simulation update loop
- Basic Tkinter visualization
- Component-based movement system
- Rendering pipeline between simulation and GUI

The evolutionary mechanics are not implemented yet.

## Current features

- Entity Component System (ECS)
- Decoupled engine, simulation, and GUI
- Real-time simulation loop
- Basic entity movement
- Desktop visualization using Tkinter

## Planned creature types

1. Herbivores
2. Predators

## Planned simulation processes

1. Natural selection affecting creature survival and reproduction
2. Inherited genes influencing creature traits
3. Gene-based behavior
4. Mutations during gene transfer

## Planned simulation controls

1. Adjusting initial creature population
2. Controlling vegetation distribution
3. Changing simulation speed

## Tech stack

- Python
- Tkinter (desktop GUI)

## Architecture

The project follows an ECS-inspired architecture with separated engine, ECS, simulation, and visualization layers.

Project structure:

- `engine` — application loop, timing control, and communication between the simulation and GUI
- `ecs` — entity-component-system core responsible for entity management, component storage, querying, and system coordination
- `simulation` — simulation logic, components, and systems implementing world behavior
- `gui` — visualization layer responsible for rendering the simulation state

The ECS core consists of:

- `EntityManager` — creates and manages entity identifiers
- `ComponentManager` — stores components and provides efficient component queries
- `SystemManager` — manages and updates simulation systems

The visualization layer is intentionally separated from the simulation logic, making it possible to support multiple frontends in the future:

- Desktop application (implemented)
- Web application (planned)

## Running

Development entry point:

```bash
python main.py
```

Running the project opens a simple Tkinter window where entities move around the simulated world.