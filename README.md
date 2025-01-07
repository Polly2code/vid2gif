# Video to GIF Converter

A simple Python script to convert video files to GIF format with options to resize and adjust playback speed.

## Features

- Convert any video format supported by moviepy to GIF
- Resize output GIF with a scaling factor
- Adjust playback speed
- Simple command-line interface

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone git@github.com:Polly2code/vid2gif.git
   cd vid2gif
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Follow the prompts:
   - Enter the path to your video file
   - Enter resize factor (e.g., 1.0 for original size, 0.5 for half size)
   - Enter speed factor (e.g., 1.0 for original speed, 2.0 for double speed)

## Demo

Here's a demonstration of converting a video to GIF:

![Demo](demo.gif)
