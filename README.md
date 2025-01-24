# Django Countries Metadata

## Requirements

- Python 3.x
- Django >= 3.0

## Model Metadata

The `Country` model represents comprehensive country information with the following key characteristics:

- **Database Model**: Django ORM Model
- **Primary Purpose**: Store detailed metadata about countries
- **Key Fields**: 
  - Identification: name, alpha2Code, alpha3Code, numericCode
  - Geographic: capital, region, subregion, latlng
  - Demographics: population, area, demonym
  - Cultural: languages, currencies, nativeName
  - Connectivity: callingCodes, topLevelDomain
  - Additional: flag, borders, timezones

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mecatheclau/Django-countries-metadata.git
   cd django-countries-metadata
   ```

2. Set up virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Load country data:
   ```bash
   python manage.py loaddata country/fixtures/countries.json
   ```

## Usage

Once installed, you can query country data through Django's ORM:

```python
from country.models import Country

# Get all countries
all_countries = Country.objects.all()

# Filter countries by region
european_countries = Country.objects.filter(region='Europe')
```