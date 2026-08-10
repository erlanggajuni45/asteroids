# Asteroids

Asteroids is a simple 2D arcade-style game built with Python and Pygame. The player controls a spaceship that can rotate, move forward, and shoot incoming asteroids. When an asteroid is hit, it splits into smaller asteroids, and the game ends if the player collides with one.

## Features

- Classic arcade-style movement and shooting
- Procedurally spawned asteroid field
- Asteroids split into smaller pieces after being hit
- Lightweight game loop with basic collision handling
- Game event and state logging for debugging and analysis

## Controls

- W: move forward
- A: turn left
- D: turn right
- S: move backward
- Space: shoot

## Tech Stack

- Python 3.11+
- Pygame 2.6.1
- uv for project management and running the app

## Project Structure

- main.py: game entry point and main loop
- player.py: player ship logic and controls
- asteroid.py: asteroid behavior and splitting
- asteroidfield.py: asteroid spawning logic
- shot.py: player projectile behavior
- constants.py: gameplay tuning values
- logger.py: event and game-state logging

## Getting Started

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Run the game:
   ```bash
   uv run asteroids
   ```

   or:

   ```bash
   python main.py
   ```

## Notes

The project includes JSONL logging files for game events and state snapshots, which can be useful for debugging or studying gameplay behavior over time.
