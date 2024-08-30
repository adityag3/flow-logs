import csv
from typing import List, Dict


class CSVHandler:
    """A class to handle reading from and writing to CSV files."""

    @staticmethod
    def read_file(file_path: str) -> List[Dict]:
        """
        Reads a CSV file and returns its contents as a list of dictionaries.

        :param file_path: Path to the CSV file.
        :return: List of dictionaries representing the CSV rows.
        """
        data = []
        try:
            with open(file_path, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        return data

    @staticmethod
    def write_file(file_path: str, data: List[List[str]], fieldnames: List[str]) -> None:
        """
        Writes a list of dictionaries to a CSV file.

        :param file_path: Path to the CSV file.
        :param data: List of dictionaries to write to the CSV file.
        :param fieldnames: List of field names (column headers) for the CSV file.
        """
        try:
            with open(file_path, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()  # Write the column headers

                for row in data:
                    writer.writerow(row)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
