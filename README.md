# DataExtraction
Creates a script that generates a list of dictionaries about files in the working directory. Then prints the list.


# File Info Collector

This project generates a list of dictionaries containing basic information (filename and size) about the files in the current working directory. It uses Python's `os` module to list files and gather file details.

## Table of Contents

- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Customization](#customization)
- [License](#license)

## Requirements

To run this project, you need the following:

- Python 3.x installed on your system.
- No additional libraries are required; this project uses the built-in `os` module.

## How It Works

The script performs the following tasks:

1. Lists files in the current working directory using `os.listdir()`.
2. Checks each item to see if it's a file (ignores directories).
3. Collects the filename and file size for each file.
4. Stores this information in a list of dictionaries.
5. Prints the list of dictionaries.

Each dictionary contains the filename and the size of the file in bytes.

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3 installed by running:

    \`\`\`bash
    python --version
    \`\`\`

3. Navigate to the project directory:

    \`\`\`bash
    cd /path/to/project
    \`\`\`

## Usage

To use this project, follow these steps:

1. Open a terminal or command prompt in the project directory.
2. Run the script using Python:

    \`\`\`bash
    python file_info_collector.py
    \`\`\`

The script will output a list of dictionaries containing the filename and size of each file in the current directory.

## Example Output

Here's an example of what the output might look like:

\`\`\`json
[
    {"filename": "example.txt", "size": 1024},
    {"filename": "image.jpg", "size": 2048}
]
\`\`\`

Each dictionary contains the following information:
- \`filename\`: The name of the file.
- \`size\`: The size of the file in bytes.

## Customization

If you want to collect additional information, such as the absolute path or last modified time, you can modify the code by adding more fields to the dictionary. Here's an example of how to include the absolute path and last modified time:

\`\`\`python
file_info = {
    'filename': file,
    'size': get_size(file),
    'absolute_path': get_absolute_path(file),  # Absolute file path
    'last_modified': get_last_modified(file)   # Last modified timestamp
}
\`\`\`

You can also adjust the script to exclude certain files or directories based on your needs.

## License

This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.
