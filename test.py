import pytest
import os
from main import text_file_filterer

@pytest.fixture
def create_test_file():
    filename = "test_input.txt"
    content = """My name is Mykyta.
My name is not Mykyta.
I am not Mykyta.
I am Igor.
He is Mykyta.
He is Igor.
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    yield filename

    os.remove(filename)
    if os.path.exists("filtered.txt"):
        os.remove("filtered.txt")