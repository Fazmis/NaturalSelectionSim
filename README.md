# NaturalSelectionSim

Natural selection simulation written in Python.

## About

This project is a simulation of evolutionary processes based on natural selection.

The goal is to create a system where creatures can evolve through interactions with the environment, inherited traits, and natural selection.

## Status

Work in progress.

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

The project uses an ECS-inspired architecture with separated engine, ECS, simulation, and visualization layers.

The project is divided into:

- `engine` — application loop, timing control, and simulation updates
- `ecs` — entity-component-system core responsible for entity management, component storage, and system coordination
- `simulation` — natural selection simulation logic, including simulation-specific components and systems
- `gui` — visualization layer responsible for rendering simulation state

The ECS core consists of:

- `EntityManager` — creates and manages entity identifiers
- `ComponentManager` — stores components and manages entity-component relationships
- `SystemManager` — manages and updates simulation systems

The GUI layer is separated from simulation logic and is designed to support multiple implementations:

- Desktop application
- Web application (planned)

## Running

Development entry point:

```bash
python main.py