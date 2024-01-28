# NSE India Index API

This Django project provides REST API endpoints for accessing historical index data obtained from the NSE India website.

## Features

- Django models for storing index data and daily price data
- Management commands for importing data from CSV files into the database
- REST API endpoints for retrieving index and daily price data
- Support for filtering, pagination, and data ranges in API responses
- User-friendly admin interface for uploading CSV files and managing data

## Installation

1. Clone the repository:

git clone https://github.com/Yashi5108/django_proj.git


2. Install dependencies:

pip install -r requirements.txt

3. Apply database migrations:

python manage.py makemigrations
python manage.py migrate


4. Create a superuser account:

python manage.py createsuperuser


5. Run the development server:

python manage.py runserver


6. Access the Django admin interface at `http://localhost:8000/admin` to upload CSV files and manage data.

## Usage

- Use the Django admin interface to upload CSV files containing index and daily price data.
- Use the provided REST API endpoints to retrieve index and daily price data.
- Customize and extend the project as needed to meet your requirements.

## API Endpoints

### Indexes

- `/api/indexes/`: List all indexes
- `/api/indexes/<index_id>/`: Retrieve details of a specific index

### Daily Prices

- `/api/daily-prices/`: List all daily prices
- `/api/daily-prices/<price_id>/`: Retrieve details of a specific daily price
- Additional filtering options are available for each column (e.g., open_price, high_price, etc.)

## Management Commands

- `python manage.py import_indexes <csv_file_path>`: Import index data from a CSV file
- `python manage.py import_daily_prices <csv_file_path>`: Import daily price data from a CSV file

## Authors

- [Yashi Gupta](https://github.com/Yashi5108)
