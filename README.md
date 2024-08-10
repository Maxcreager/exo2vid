# exo2vid
EXO2VID - A forensic tool for reassembling and repairing fragmented EXO video files. This script identifies, reassembles, and optionally repairs EXO files, making them viewable as a standard video format (MP4).

# EXO2VID

**EXO2VID** is a forensic tool designed to reassemble fragmented EXO video files, commonly used by some mobile applications to store partial video data. The tool allows investigators to merge these fragments into a single video file and repair it, making the video playable in a standard media player.

## Features

- **Reassemble EXO Files**: Automatically locates and combines EXO video fragments into a complete MP4 file.
- **Repair Video Files**: Optionally repairs the reassembled video file using `ffmpeg` to ensure compatibility and correct playback.
- **Command-Line Interface**: Flexible and easy-to-use CLI for specifying input directories and output files.

## Requirements

- Python 3.x
- `ffmpeg` (Must be installed and accessible via the system PATH or specified in the script)
- `ffmpeg-python` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/exo2vid.git
    cd exo2vid
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure `ffmpeg` is installed:**

   - Download `ffmpeg` from [FFmpeg Download](https://ffmpeg.org/download.html).
   - Add `ffmpeg` to your system's PATH or modify the script to specify the path to `ffmpeg.exe`.

## Usage

### Command-Line Arguments

- `-i`, `--input` : Specifies the input directory containing the EXO files.
- `-o`, `--output`: Specifies the output file path (including filename) for the reassembled video.
- `-r`, `--repair`: (Optional) Repairs the reassembled video file using `ffmpeg`.

