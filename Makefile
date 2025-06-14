.PHONY: venv install migrate runserver offers start

# Create virtual environment
venv:
	python -m venv .venv

# Install dependencies
install: venv
	. .venv/bin/activate && pip install -r requirements.txt

# Make and apply migrations
migrate:
	cd webapp && python manage.py makemigrations && python manage.py migrate

# Generate example offers
offers:
	cd webapp && python scripts/create_offers.py

# Run the development server
runserver:
	cd webapp && python manage.py runserver

# Run all above
start: install migrate offers runserver