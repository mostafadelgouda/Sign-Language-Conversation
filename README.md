# Sign Language Conversation

A Python-based desktop application that facilitates seamless communication by translating Arabic Sign Language to voice and vice versa. The application utilizes deep learning models for hand gesture detection and a user-friendly interface built with Tkinter.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Sign Language Conversation application aims to bridge the communication gap between deaf and hearing individuals by translating sign language gestures into audible sentences and vice versa.

## Features
- **Sign Language Detection**: Uses VGG16 model for accurate detection of Arabic Sign Language gestures.
- **Audio Conversion**: Converts detected signs into audible sentences using Pyaudio.
- **User-friendly Interface**: Built with Tkinter for an enhanced user experience.

## Technologies Used
- **Python**: Main programming language.
- **Deep Learning**: VGG16 model for hand gesture detection.
- **Tkinter**: For building the graphical user interface.
- **Pyaudio**: For audio processing.
- **MediaPipe**: For hand tracking and gesture recognition.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mostafadelgouda/Sign-Language-Conversation.git
    cd Sign-Language-Conversation
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python app.py
    ```
2. Follow the on-screen instructions to translate sign language gestures to voice and vice versa.

## Project Structure
- `app.py`: Main application file.
- `models/`: Contains the VGG16 model and other related files.
- `gui/`: Tkinter-based user interface components.
- `audio/`: Audio processing scripts.
- `requirements.txt`: List of dependencies.

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
