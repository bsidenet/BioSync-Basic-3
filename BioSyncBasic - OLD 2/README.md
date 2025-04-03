# BioSync Basic

BioSync Basic is a Django project designed for managing blood pressure measurements. This application allows users to record, track, and analyze their blood pressure readings over time.

## Features

- User-friendly interface for entering blood pressure measurements.
- Ability to view historical data and trends.
- Admin interface for managing users and data.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd BioSyncBasic
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin interface to manage blood pressure data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.