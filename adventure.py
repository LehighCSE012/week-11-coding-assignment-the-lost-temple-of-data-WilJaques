# Your code goes here
import pandas as pd
import re

# 1. Load Artifact Data (Excel)

# Function: load_artifact_data(excel_filepath)

# Input: excel_filepath (string): The path to the artifacts.xlsx file.

# Action:

# Read the data specifically from the sheet named 'Main Chamber'.

# The actual table data starts after the first 3 rows (skip these introductory rows).

# Use Pandas to read this data into a DataFrame.

# Return: A Pandas DataFrame containing the artifact data from the specified sheet, skipping the initial rows.

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    # Hint: Use pd.read_excel, specify sheet_name and skiprows
    # Replace 'pass' with your code
    return pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)

    # return the resulting DataFrame

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    # Hint: Use pd.read_csv, specify the separator for tabs ('\t')
    # Replace 'pass' with your code
    return pd.read_csv(tsv_filepath, sep='\t')
    # return the resulting DataFrame

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for MM/DD/YYYY format.
    # Pattern idea: r"\d{2}/\d{2}/\d{4}"
    # Replace 'pass' with your code

    return re.findall(r"\d{2}/\d{2}/\d{4}", journal_text)
    # return the list of found dates

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for AZMAR- followed by 3 digits.
    # Pattern idea: r"AZMAR-\d{3}"
    # Replace 'pass' with your code
    return re.findall(r"AZMAR-\d{3}", journal_text)
    # return the list of found codes


# --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
    # Define file paths (adjust if your files are located elsewhere)
    excel_file = 'artifacts.xlsx'
    tsv_file = 'locations.tsv'
    journal_file = 'journal.txt'

    print(f"--- Loading Artifact Data from {excel_file} ---")
    try:
        artifacts_df = load_artifact_data(excel_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {excel_file}")

    print(f"\n--- Loading Location Notes from {tsv_file} ---")
    try:
        locations_df = load_location_notes(tsv_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {tsv_file}")

    print(f"\n--- Processing Journal from {journal_file} ---")
    try:
        with open(journal_file, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        dates = extract_journal_dates(journal_content)
        print(f"Found dates: {dates}")

        print("\nExtracting Secret Codes...")
        codes = extract_secret_codes(journal_content)
        print(f"Found codes: {codes}")

    except FileNotFoundError:
        print(f"Error: File not found at {journal_file}")
