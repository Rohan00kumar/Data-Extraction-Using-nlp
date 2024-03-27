# Text Analysis from Web Articles

This Python script extracts text from URLs and performs various text analyses including sentiment analysis, readability assessment, and linguistic complexity metrics. It utilizes libraries such as NLTK, BeautifulSoup, TextBlob, and Syllapy.

## Dependencies

- Python 3.x
- pandas
- requests
- beautifulsoup4
- nltk
- textblob
- syllapy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your input data in an Excel file (`Input.xlsx`) with columns 'URL_ID' and 'URL' containing the IDs and URLs of the articles to analyze.

2. Run the script:

    ```bash
    python text_analysis.py
    ```

3. The script will extract text from each URL, perform text analysis, and save the results in an Excel file (`Output.xlsx`).

## Input Data Format

The input data should be provided in an Excel file (`Input.xlsx`) with the following format:

| URL_ID | URL              |
|--------|------------------|
| 1      | http://example1  |
| 2      | http://example2  |
| ...    | ...              |

## Output Data Format

The output data is saved in an Excel file (`Output.xlsx`) with the following columns:

| URL_ID | POSITIVE SCORE | NEGATIVE SCORE | POLARITY SCORE | SUBJECTIVITY SCORE | AVG SENTENCE LENGTH | PERCENTAGE OF COMPLEX WORDS | FOG INDEX | AVG NUMBER OF WORDS PER SENTENCE | COMPLEX WORD COUNT | WORD COUNT | SYLLABLE PER WORD | PERSONAL PRONOUNS | AVG WORD LENGTH |
|--------|----------------|----------------|----------------|--------------------|---------------------|------------------------------|-----------|----------------------------------|---------------------|-------------|---------------------|-------------------|-----------------|
| ...    | ...            | ...            | ...            | ...                | ...                 | ...                          | ...       | ...                              | ...                 | ...         | ...                 | ...               | ...             |

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

[Insert License Here]

## Acknowledgments

- This project utilizes various Python libraries including NLTK, BeautifulSoup, TextBlob, and Syllapy.
