"""Utility functions used by the mcqgenerator app."""
import json
import traceback

import PyPDF2
from PyPDF2 import PdfReader


class PdfReadError(Exception):
    """Exception raised for errors in reading a PDF file."""

    def __init__(self: "PdfReadError") -> None:
        """Initialize the exception."""
        self.message = "Error reading PDF file"
        super().__init__(self.message)


class UnsupportedFileTypeError(Exception):
    """Exception raised for unsupported file types."""

    def __init__(self: "UnsupportedFileTypeError", filetype: str) -> None:
        """Initialize the exception."""
        self.filetype = filetype
        self.message = (
            f"Unsupported file type: {filetype}. Only PDF and TXT files are supported."
        )
        super().__init__(self.message)


def read_file(file: PyPDF2.PdfFileReader) -> str:
    """Read a pdf or txt file and returns the text."""
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

        except Exception as e:
            raise PdfReadError from e

        else:
            return text

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise UnsupportedFileTypeError(filetype=file.name)


def get_table_data(quiz_str: str) -> [{}]:
    """Convert the quiz from str to dict and get table."""
    try:
        # convert the quiz from str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        # Iterate over the quiz dictionnary and extract the required information
        for mcq in quiz_dict["mcqs"]:
            question = mcq["question"]
            options = " | ".join(
                [
                    f"{option_key}: {option_value}"
                    for option_key, option_value in mcq["options"].items()
                ],
            )
            correct_answer = mcq["answer"]

            quiz_table_data.append(
                {
                    "MCQ": question,
                    "Choices": options,
                    "Correct": correct_answer,
                },
            )

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

    else:
        return quiz_table_data
