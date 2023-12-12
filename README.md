# Text Data Preprocessing Python Script

This Python script performs text data preprocessing, cleaning, and sentence extraction. It is designed to prepare textual data for natural language processing (NLP) or machine learning applications by applying various text cleaning techniques.

## Features

- Removes links, hashtags, numeric expressions, and special characters.
- Converts text to lowercase for consistent analysis.
- Removes stopwords to focus on meaningful content.
- Extracts sentences from each line in the input file.
- Removes duplicate sentences for a cleaner dataset.

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Poeron/Text-Data-Preprocessing-Python.git
    cd Text-Data-Preprocessing-Python
    ```

2. **Install Dependencies:**

    ```bash
    pip install nltk
    ```

3. **Run the Script:**

    Open the script (`text_preprocessing.py`) in a code editor and specify your input and output file paths directly within the script. Look for the lines similar to:

    ```python
    input_file_path = "input.txt"
    output_file_path = "output.txt"
    ```

    Update these lines with the paths to your input and desired output files.

4. **Execute the Script:**

    Run the script using your Python interpreter:

    ```bash
    python text_preprocessing.py
    ```

## Requirements

- Python 3.x
- nltk library

## How it Works

- The script uses regular expressions, the `nltk` library, and basic string manipulation for text cleaning.
- Sentence extraction is performed using the `nltk.sent_tokenize` function.
- Duplicate lines are removed to enhance dataset quality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [nltk](https://www.nltk.org/) library was used for natural language processing tasks.
