from typing import List


class FileHandler:
    """A class to handle reading from and writing to text files."""

    @staticmethod
    def read_file(file_path: str, seperator: str = None) -> List[str]:
        """
        Reads a Text file and returns its contents as a list of dictionaries.
        :param seperator:
        :param file_path: Path to the Text file.
        :return: List of Strings representing the rows in file.
        """
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if seperator:
                        line = line.split(seperator)
                    data.append(line)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        return data

    @staticmethod
    def write_file(file_path: str, data: str) -> None:
        """
        Writes a string to normal file.

        :param file_path: Path to the data file.
        :param data: String to write to the data file.
        """
        try:
            with open(file_path, 'w') as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
