# Color Identifier 

## Introduction
This project is designed to identify the name of a color based on its RGB values. It utilizes the `webcolors` library in Python, which provides a mapping between RGB values and color names from the CSS3 specification. Additionally, it visualizes the color using `matplotlib`.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Methodology](#methodology)
- [Result](#result)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
To get started with this project, you can clone the repository to your local machine and follow the instructions provided in the README.

## Prerequisites
Before running the code, ensure you have the following dependencies installed:

- Python 3.x
- `webcolors` library
- `matplotlib` library

You can install these dependencies using pip:
```bash
pip install webcolors matplotlib
```
## Usage
1. Run the Python script `color_identifier.py`.
2. Specify the RGB values of the color you want to identify by modifying the `color` variable (e.g., `color = (223, 241, 224)`).
3. The script will attempt to identify the color name. If it can't find an exact match, it will find the closest color name.
4. The color and its name will be displayed in the terminal, and a visual representation of the color will be shown using `matplotlib`.

## Methodology
The color identification process involves the following steps:
- Mapping RGB values to color names using the `webcolors` library.
- Finding the closest color name if an exact match is not found.

## Result
The script will output the name of the identified color or the closest matching color name, along with a visual representation of the color.

## Contributing
Contributions to this project are welcome. You can contribute by improving the accuracy of color identification or enhancing the visualization of colors.
