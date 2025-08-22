Pygame Asteroids

A classic arcade-style asteroids game built with Python and the Pygame library. Navigate your spaceship through a treacherous asteroid field, blasting space rocks to bits while avoiding a fatal collision.
Gameplay

You control a spaceship in a 2D environment. Asteroids will spawn and move across the screen. Your objective is to destroy as many asteroids as possible by shooting them. When an asteroid is hit, it will split into smaller pieces. Colliding with any asteroid will immediately end the game.

Features:

    Player Control: Full control over the spaceship's movement and rotation.

    Shooting Mechanic: Fire projectiles to destroy asteroids.

    Dynamic Asteroids: Asteroids spawn at random locations and split into smaller fragments when destroyed.

    Collision Detection: The game ends if the player's ship collides with an asteroid.

How to Play:

    Up Arrow: Thrust forward

    Left/Right Arrows: Rotate the ship

    Spacebar: Shoot

Installation & Setup:

To run this game, you'll need to have Python and Pygame installed on your system.

    Clone the repository (or download the source files):

    git clone https://your-repository-url.git
    cd your-project-directory

    Install Pygame:
    If you don't have Pygame installed, you can install it using pip:

    pip install pygame

    Run the game:
    Execute the main script from your terminal:

    python main.py

Project Structure:

The project is organized into several Python files:

    main.py: The main entry point for the game. It contains the primary game loop and handles event processing.

    player.py: Defines the Player and Shot classes, managing the spaceship's behavior and projectiles.

    asteroid.py: Defines the Asteroid class, responsible for the behavior of individual asteroids.

    asteroidfield.py: Manages the spawning and overall behavior of the collection of asteroids.

    constants.py: Stores all constant values used throughout the project, such as screen dimensions and colors.
