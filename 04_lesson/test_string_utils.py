import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123Test", "123Test"),  # Числа в начале строки
    (" Тест", " Тест"),  # Строка с пробелом в начале
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.capitalize
@pytest.mark.negative
def test_capitalize_none(string_utils):
    assert string_utils.capitalize(None) == ""


@pytest.mark.trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" world", "world"),
    ("  123", "123"),
    ("   привет", "привет"),
    ("   04 апреля 2023", "04 апреля 2023")  # Строка с датой и пробелами
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [  # Объединил в один тест
    ("skypro", "skypro"),
    ("world ", "world "),
    ("123  ", "123  "),
    ("   skypro   ", "skypro   "),  # Test that trailing spaces are not removed
    ("Тест", "Тест"),   # Тест не пустая строка
])
def test_trim_no_leading_whitespace(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("123", "2", True),
    ("Тест", "с", True),   # Не пустая строка
    ("04 апреля 2023", "а", True),   # Строка с пробелами
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.contains
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "u", False),
    ("123", "4", False),
    ("", "a", False),  # Пустая строка
    ("   ", "a", False),  # Строка с пробелом
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello", "l", "heo"),  # Удаление нескольких символов
    ("Тест", "т", "Тес"),  # Не пустая строка
    ("04 апреля 2023", " ", "04апреля2023"),  # Строка с пробелами
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),  # Символа нет в строке
    ("123", "a", "123"),
    ("", "a", ""),  # Пустая строка
    ("   ", "a", "   "),  # Строка с пробелом
])
def test_delete_symbol_no_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
