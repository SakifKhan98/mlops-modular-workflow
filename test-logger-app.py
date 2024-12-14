import sys

from src.exception import CustomException
from src.logger import logging

# Define a function that raises a custom exception
def example_function():
  try:
    # Simulate a division by zero error
    x = 10
    y = 0
    result = x / y
  except ZeroDivisionError as e:
    # Raise a custom exception with detailed error information
    raise CustomException(e, sys)
  
if __name__ == "__main__":
  try:
    example_function()
  except CustomException as e:
    print(e)