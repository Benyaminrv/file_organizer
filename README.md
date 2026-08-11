# File Organizer

A Python CLI tool that automatically organizes files in a directory
based on their file extensions.

## Features

- Scan files in a target directory
- Detect file extensions using Regex
- Categorize files
- Create category folders automatically
- Move files into their corresponding folders
- Handle duplicate files
- Handle permission errors
- Display organization statistics

## Categories

- Images
- Videos
- Documents
- Apps
- Audio
- Compressed
- Other

## Requirements

- Python 3.14+
  
## How to Run

Run:

    python main.py

Then enter the target directory when prompted.

## Project Structure

    main.py        # CLI and user interaction
    functions.py   # File scanning and organization logic
