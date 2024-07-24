# Weather Forecast API

An API to provide weather forecasts for different cities. This project uses Python with Flask, SQLite, and the OpenWeatherMap API.

## Features

- User registration and authentication
- Fetch weather data from an external API
- Store user favorite locations
- Provide current weather and forecast for favorite locations

## Technologies

- Python
- Flask
- SQLite
- OpenWeatherMap API

## Setup

### Prerequisites

- Python 3.6+
- Virtualenv (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fujahgabriel/Weather-Forecast-API.git
   cd Weather-Forecast-API
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

    Create a .env file in the root directory and add the following:

    ```bash
    SECRET_KEY=your_secret_key
    JWT_SECRET_KEY=your_jwt_secret_key
    WEATHER_API_KEY=your_openweathermap_api_key
    ```

5. Database Setup
   Initialize the SQLite database:

    ```bash
    python setup_db.py
    ```

6. Start the development server:

   ```bash
   python app.py
   ```

## Running Tests
    Unit tests are provided to test the functionality of the API.
    Make sure the virtual environment is activated.

    ```bash
    python -m unittest discover -s test
    ```

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
