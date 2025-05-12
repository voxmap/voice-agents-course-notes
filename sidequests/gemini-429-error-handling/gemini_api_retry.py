import time
import random
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# --- Backoff Function ---
def backoff(attempt, base_delay=1.0, max_delay=60):
    """
    Backoff function to prevent resource exhaustion errors
    """
    delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
    print(f"Rate limit hit or server busy. Retrying in {delay:.2f} seconds...")
    time.sleep(delay)

# --- Gemini API Call with Retry ---
def gemini_call(prompt, model, max_attempts=10):
    """
    A simplified example of calling the Gemini API with a retry mechanism
    for ResourceExhausted errors.
    """
    for attempt in range(max_attempts):
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            content = model.generate_content(prompt)
            response = content.text
            return response

        except ResourceExhausted as e:
            # TODO: Log the error
            print(f"ResourceExhausted error: {e}")
            if attempt < max_attempts - 1: # If not the last attempt
                backoff(attempt)  # Perform backoff
            else:
                print(f"Max retry attempts ({max_attempts}) reached. Failed to get response.")
                raise RuntimeError(f"Failed after {max_attempts} attempts due to repeated ResourceExhausted errors.")