from string_utils import StringUtils


string_utils = StringUtils()

def test_positive_capitalize():
    result = string_utils.capitalize("домашка")
    assert result == "Домашка"

def test_negative_capitalize():
    result = string_utils.capitalize("Домашка")
    assert result == "Домашка"

def test_negative_capitalize():
    result = string_utils.capitalize("123")
    assert result == "123"

def test_positive_trim():
    result = string_utils.trim("    пробелы")
    assert result == "пробелы"

def test_negative_trim():
    result = string_utils.trim("безпробелов")
    assert result == "безпробелов"

def test_positive_contains2():
    result = string_utils.contains("Asdfg", "s")
    assert result == True

def test_negative_contains2():
    result = string_utils.contains("Asdfg", "n")
    assert result == False

def test_positive_delete_symbol():
    result = string_utils.delete_symbol("Vivobook", "i")
    assert result == "Vvobook"

def test_negative_delete_symbol():
    result = string_utils.delete_symbol("Vivobook", "a")
    assert result == "Vivobook"


