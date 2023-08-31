# Conversion Tool

The Conversion Tool is a simple application built in Python that allows users to convert PDF files, JPG images, and PNG images to different formats. The application provides a graphical user interface (GUI) using the tkinter library and utilizes the pillow library for image conversions.

## Prerequisites

Before running the Conversion Tool, ensure that you have the following installed:

- Python (version 3.6 or higher)
- tkinter library (usually included with Python)
- pillow library (can be installed via pip)

## Installation

1. Clone the repository to your local machine:

```shell
git clone https://github.com//ali-elrogbany/conversion-hub.git
```

2. Navigate to the project directory:

```shell
cd conversion-hub
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Run the application by executing the `main.py` file.
2. The Conversion Tool GUI will appear.
3. Click the "Browse Files" button to select the file you want to convert.
4. Choose the desired output format from the available options.
5. Click the corresponding conversion button to initiate the conversion process.
6. Once the conversion is complete, the converted file will be saved in the same directory as the source file. 

## Custom Conversion Class

The Conversion Tool includes a custom ConversionUtils class that handles the conversion process. The class provides methods for converting images to JPG, PDF, and PNG formats. You can find the implementation of the class in the `ConversionUtils.py` file.

## Custom File Utilities Class

The Conversion Tool also includes a File class that provides file-related utilities. It allows users to browse and select files for conversion. You can find the implementation of the class in the `FileUtilities.py` file.

## Contributing

Contributions to the Conversion Tool are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the GitHub repository.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

The Conversion Tool was developed using the following libraries:

- [Python ↗](https://www.python.org/)
- [tkinter ↗](https://docs.python.org/3/library/tkinter.html)
- [pillow ↗](https://pillow.readthedocs.io/)

Special thanks to the developers and contributors of these open-source libraries.

Enjoy using the Conversion Tool!
