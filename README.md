# battery-saver-toggle

**battery-saver-toggle** is a Python application that provides an easy way to toggle the battery conservation mode on laptops running Ubuntu and other Linux distributions. The program uses a system tray indicator to display the current state of battery conservation mode and allows toggling it with a single click.

## Requirements

- Python 3
- GTK 3
- AppIndicator3
- Python `gi` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ivodraganov/battery-saver-toggle.git
    cd battery-saver-toggle
    ```

2. Install the required libraries:
    ```bash
    sudo apt install python3-gi python3-gi-cairo gir1.2-appindicator3-0.1
    ```

3. Run the script:
    ```bash
    python3 battery-saver-toggle.py
    ```

## Usage

The application will start in the system tray and display the battery icon. There will be two options in the context menu:
- Toggle the battery conservation mode
- Exit the application

The program will display the current state of battery conservation mode and allow easy toggling between the enabled and disabled state.

## License

This project is open source and licensed under the MIT License.

