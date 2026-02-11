# 🚀 Asteroids Replica

A classic asteroids arcade game replica built with Python and Pygame, featuring clean object-oriented architecture and comprehensive logging for gameplay analysis.

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.6.1-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎮 Features

### Classic Gameplay
- **Ship Controls**: Smooth rotation and thrust-based movement
- **Shooting Mechanics**: Cooldown-based projectile system
- **Asteroid Physics**: Realistic splitting mechanics with three size tiers
- **Collision Detection**: Precise circle-based collision system
- **Progressive Difficulty**: Continuous asteroid spawning from screen edges

### Technical Features
- **60 FPS Game Loop**: Smooth gameplay with delta time calculations
- **Sprite Group Management**: Efficient rendering and update systems
- **Comprehensive Logging**: Game state and event tracking for analysis
- **Modern Python**: Type hints, proper packaging with `pyproject.toml`
- **Clean Architecture**: Modular design with separation of concerns

## 🛠️ Installation

### Prerequisites
- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd asteroids
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

### Alternative: Using pip
If you prefer not to use uv:
```bash
pip install pygame==2.6.1
```

## 🎯 How to Play

### Starting the Game
```bash
python main.py
```

### Controls
| Key | Action |
|-----|--------|
| **W** | Thrust forward |
| **A** | Rotate left |
| **D** | Rotate right |
| **Space** | Fire shot |
| **ESC** | Exit game |

### Gameplay
- Navigate your spaceship through an asteroid field
- Shoot asteroids to break them into smaller pieces
- Large asteroids → Medium asteroids → Small asteroids → Destroyed
- Avoid collisions with asteroids to survive
- New asteroids continuously spawn from screen edges

## 🏗️ Architecture

### Design Patterns
- **Object-Oriented Design**: All game objects inherit from a common `CircleShape` base class
- **Container Pattern**: Automatic sprite group registration for efficient management
- **Component-Based Architecture**: Clear separation of physics, rendering, and game logic

### Core Components

#### Base Classes
- **`CircleShape`** (`circleshape.py`): Abstract base class for all circular game objects with collision detection

#### Game Objects
- **`Player`** (`player.py`): Ship controls, movement physics, and shooting mechanics
- **`Asteroid`** (`asteroids.py`): Asteroid objects with splitting behavior and three size tiers
- **`Shot`** (`shot.py`): Projectile system with linear motion
- **`AsteroidField`** (`asteroidfield.py`): Spawning system that generates asteroids from screen edges

#### Systems
- **`main.py`**: Game loop, sprite group management, and collision detection
- **`constants.py`**: Game configuration and physics parameters
- **`logger.py`): Comprehensive game state and event logging system

## 📁 File Structure

```
asteroids/
├── main.py                 # Main game loop and entry point
├── circleshape.py          # Base class for circular objects
├── player.py               # Player ship implementation
├── asteroids.py            # Asteroid objects and splitting logic
├── shot.py                 # Bullet/projectile system
├── asteroidfield.py        # Asteroid spawning management
├── constants.py            # Game configuration and constants
├── logger.py               # Game state and event logging
├── pyproject.toml          # Python project configuration
├── uv.lock                 # Dependency lock file
├── .python-version         # Python version specification
├── .gitignore              # Git ignore rules
├── game_events.jsonl       # Event log file
├── game_state.jsonl        # State log file
└── README.md               # This file
```

## ⚙️ Configuration

### Game Constants (`constants.py`)
```python
# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Player
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_COOLDOWN = 0.3

# Asteroids
ASTEROID_MIN_RADIUS = 20
ASTEROID_MAX_RADIUS = 60
ASTEROID_SPAWN_RATE = 0.8
ASTEROID_KINDS = 3

# Shots
SHOT_RADIUS = 5
SHOT_SPEED = 500
```

### Customization
You can modify gameplay by adjusting constants in `constants.py`:
- Change spawn rates for difficulty
- Adjust ship speeds and turn rates
- Modify asteroid sizes and quantities
- Tweak shooting cooldown and speed

## 📊 Logging & Debugging

### Logging System
The game includes comprehensive logging for gameplay analysis:

- **State Logging**: Records positions, velocities, and object counts every second
- **Event Logging**: Tracks collisions, asteroid splits, and game over events
- **Time-Limited**: Automatically stops logging after 16 seconds
- **JSON Format**: Structured logging for easy analysis

### Log Files
- `game_state.jsonl`: State snapshots for analysis
- `game_events.jsonl`: Event timeline for debugging

### Using the Logs
The logs can be used to:
- Analyze gameplay patterns
- Debug collision issues
- Balance difficulty
- Track performance metrics

## 🔧 Development

### Code Quality
- Clean, readable code structure
- Proper separation of concerns
- Efficient sprite group management
- Modern Python practices
- Comprehensive type hints

### Extending the Game

#### Adding New Features
The modular architecture makes it easy to add:
- Power-ups and special weapons
- Enemy ships with AI
- Particle effects for explosions
- Sound effects and music
- Score tracking and high scores
- Multiple difficulty levels
- Screen wrapping for objects

#### Adding New Game Objects
1. Inherit from `CircleShape` base class
2. Implement `update()` and `draw()` methods
3. Register with appropriate sprite groups
4. Add collision handling in `main.py`

### Running Tests
```bash
# If tests are added in the future
pytest tests/
```

### Code Style
The project follows PEP 8 style guidelines with:
- 4-space indentation
- Descriptive variable names
- Proper docstrings
- Type hints where beneficial

## 🎯 Future Enhancements

### Planned Features
- [ ] Score tracking and high score system
- [ ] Sound effects and background music
- [ ] Particle effects for explosions
- [ ] Power-ups (multi-shot, shield, etc.)
- [ ] Multiple difficulty levels
- [ ] Enemy ships with basic AI
- [ ] Screen wrapping for all objects
- [ ] Pause menu and settings
- [ ] Controller support

### Performance Optimizations
- [ ] Object pooling for shots
- [ ] Spatial partitioning for collision detection
- [ ] Asset preloading
- [ ] Configurable graphics settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Classic Atari Asteroids for the game concept
- Pygame community for excellent documentation and examples
- Python game development community for best practices

## 📞 Contact

[Your Name] - [@yourusername](https://github.com/yourusername) - your.email@example.com

---

**Enjoy playing and developing with this asteroids replica! 🚀**