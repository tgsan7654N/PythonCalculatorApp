import pytest
from PyQt5.QtWidgets import QApplication, QPushButton
from calculator_app.calculator import Calculator

# Create a QApplication instance (required for PyQt5 testing)
@pytest.fixture(scope="module")
def app():
    return QApplication([])

@pytest.fixture
def calculator(app):
    return Calculator()

def test_initial_display_is_empty(calculator):
    """Test that the display is initially empty."""
    assert calculator.display.text() == ""

def test_button_clicks(calculator):
    """Test that button clicks update the display."""
    buttons = ["1", "2", "3", "+", "4"]
    for button_text in buttons:
        button = get_button_by_text(calculator, button_text)
        button.click()
    assert calculator.display.text() == "123+4"

def test_clear_button(calculator):
    """Test that the 'C' button clears the display."""
    calculator.display.setText("123+4")
    clear_button = get_button_by_text(calculator, "C")
    clear_button.click()
    assert calculator.display.text() == ""

def test_calculation(calculator):
    """Test that the calculator evaluates expressions correctly."""
    calculator.display.setText("123+4")
    equals_button = get_button_by_text(calculator, "=")
    equals_button.click()
    assert calculator.display.text() == "127"

def test_invalid_expression(calculator):
    """Test that invalid expressions are handled gracefully."""
    calculator.display.setText("123+")
    equals_button = get_button_by_text(calculator, "=")
    equals_button.click()
    assert calculator.display.text() == "Error"

# Helper function to get buttons by their text
def get_button_by_text(calculator, text):
    for button in calculator.findChildren(QPushButton):
        if button.text() == text:
            return button
    return None