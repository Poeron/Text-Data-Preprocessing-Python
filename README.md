# Text Data Preprocessing Python Script

This Python script is designed for preprocessing text data from a file. It performs various cleaning tasks such as removing links, hashtags, duplicate lines, and stopwords. Additionally, it converts the text to lowercase and eliminates numeric expressions.

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

    ```bash
    python text_preprocessing.py input.txt output.txt
    ```

    Replace `input.txt` with the path to your input file and `output.txt` with the desired output file path.

## Requirements

- Python 3.x
- nltk library

## How it Works

- The script uses regular expressions, the `nltk` library, and basic string manipulation to clean and preprocess text data.
- It removes links, hashtags, numeric expressions, special characters, and converts text to lowercase.
- Duplicate lines and empty lines are also removed, and stopwords are filtered.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The [nltk](https://www.nltk.org/) library was used for natural language processing tasks.
