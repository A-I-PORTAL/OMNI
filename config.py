import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TOKEN_ALLOWANCE = 1000  # Default token allowance
    TOKEN_PRICE = 0.01  # Price per token in dollars
