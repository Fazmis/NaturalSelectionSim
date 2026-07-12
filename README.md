# NaturalSelectionSim

Natural selection simulation written in Python.

## About

This project is a simulation demonstrating evolutionary processes based on natural selection.

## Status

Work in progress.

## Initial planned creature types:
1. Herbivores
2. Predators

## Planned simulation processes:
1. Natural selection affecting creature survival and reproduction
2. Inherited genes influencing creature traits
3. Gene-based behavior
4. Mutations during gene transfer

## Planned simulation controls:
1. Adjusting initial creature population
2. Controlling vegetation distribution
3. Changing simulation speed

## Tech stack
- Python
- Tkinter (desktop GUI)

## Architecture

ECS-inspired architecture.

The project is divided into:
- `engine` — application loop and system execution
- `simulation` — evolutionary simulation logic
- `gui` — visualization layer

The GUI layer is designed to support multiple implementations:
- Desktop application
- Web application (planned)

## Running

Development entry point:

`main.py`
