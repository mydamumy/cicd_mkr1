import pytest
from main import text_file_filterer

test_cases = [
    ("test1.txt", "hello", ["Hello world\n", "hello again\n"]),
    ("test2.txt", "test", ["Test line 1\n", "Another test case\n"]),
    ("test3.txt", "python", ["Python is great\n"]),
]


@pytest.mark.parametrize("file_name, keyword, expected_lines", test_cases)
def test_text_file_filterer(file_name, keyword, expected_lines, tmp_path):
    test_file = tmp_path / file_name
    content = """Hello world
    This is a sample text
    hello again
    Test line 1
    Another test case
    Python is great
    """
    test_file.write_text(content)

    output_file = tmp_path / "filtered.txt"

    text_file_filterer(str(test_file), keyword)

    result_lines = output_file.read_text().splitlines(keepends=True)

    result_lines = [line.strip() for line in result_lines]
    expected_lines = [line.strip() for line in expected_lines]

    assert result_lines == expected_lines, f"Очікувані рядки: {expected_lines}, але отримано: {result_lines}"

