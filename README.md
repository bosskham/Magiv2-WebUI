# Magiv2 WebUI

Magiv2 WebUI is a web-based user interface for the Magiv2 model, providing functionality for image processing and text extraction using a deep learning model. This project is based on the Magiv2 model from Hugging Face and has been adapted for easier use through a web interface.

## Features

- **Upload Chapter Pages**: Upload and process chapter pages (PNG/JPEG images).
- **Upload Character Images**: Upload and manage character images.
- **Text Extraction and Visualization**: Extract and visualize text from images.
- **Transcript Generation**: Generate and download transcripts with character names.

## Getting Started

### Prerequisites

1. Python 3.7 to 3.10.10: Ensure you have Python installed. [Download here](https://www.python.org/downloads/).
2. nVidia CUDA Toolkit 11.8: [Download here](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64).
3. **Virtual Environment** (optional but recommended): Create an isolated environment for the project.

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/bosskham/Magiv2-WebUI.git
   cd Magiv2-WebUI
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Run the WebUI:**

   ```sh
   python app.py
   ```

2. **Access the WebUI:**

   Open your web browser and go to `http://localhost:7860` to access the interface.

3. **Upload Chapter Pages and Character Images:**

   - Use the file upload fields to select and upload chapter pages and character images.
   - The interface will process the images and display results.

4. **Download Transcripts:**

   - After processing, you can download the generated transcripts with character names.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The Magiv2 model is provided by [ragavsachdeva](https://huggingface.co/ragavsachdeva/magiv2).
- This project uses components from [Gradio](https://gradio.app/) for creating the web interface.

## Contact

For any issues or questions, please open an issue in the GitHub repository or contact [boromey.han@gmail.com](mailto:your_email@example.com).

## Contributing

Contributions to the project are welcome! Please follow these steps:

1. **Fork the repository**: Create your own copy of the repository.
2. **Create a branch**: Make your changes in a new branch.
3. **Commit your changes**: Write clear and concise commit messages.
4. **Push to your fork**: Push your changes to your fork on GitHub.
5. **Submit a pull request**: Open a pull request with a description of your changes.

Please ensure that your contributions adhere to the project's coding standards and include relevant tests.

## Known Issues

- Ensure all required Python packages are installed.
- If you encounter any issues, please check the [Issues](https://github.com/bosskham/Magiv2-WebUI/issues) page for known problems and solutions.

---
