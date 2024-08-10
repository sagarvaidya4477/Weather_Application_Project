# Weather Application

This is a Python-based Weather Application built with Tkinter for the GUI and integrated with an API for fetching weather data. The application allows users to register, log in, and search for weather information by city name or geographic coordinates (latitude and longitude).

## Features

- **User Authentication:** Registration and login functionality with validation.
- **Weather Search by City:** Fetch weather data by entering a city name.
- **Weather Search by Coordinates:** Fetch weather data by entering latitude and longitude.
- **Real-Time Weather Data:** Displays current temperature, weather conditions, humidity, sunrise, sunset, and country information.
- **GUI:** A user-friendly graphical interface with enhanced visual elements.

## Requirements

- Python 3.6+
- Tkinter (usually comes pre-installed with Python)
- `requests` library for API calls

## Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/sagarvaidya4477/Weather_Application_Project.git

    cd weather-application
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application:**
    ```bash
    python app.py
    ```

2. **Login/Registration:**
   - The application starts with a login page.
   - If you're a new user, click on the "Register" button to create an account.

3. **Search Weather by City Name:**
   - After logging in, you can search for weather data by entering a city name.
   - The weather information for the city will be displayed on the screen.

4. **Search Weather by Coordinates:**
   - You can also search for weather data by entering latitude and longitude.
   - The corresponding weather information will be displayed.

## File Structure

- **app.py:** The main application file containing the GUI and logic.
- **Database.py:** Handles database operations for user authentication.
- **Api.py:** Contains methods to interact with the weather API.
- **README.md:** Project documentation.

## API Integration

The weather data is fetched from an external API. Make sure to replace the placeholder API key in `Api.py` with your actual key.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please create a pull request with a detailed description of your changes.

## Contact

For any questions or feedback, feel free to reach out to the project maintainer at vaidyasagar639@gmail.com
