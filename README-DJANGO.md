# Duke Vadis Django website

This branch contains a Django-powered six-section website: Home, About Us, Services, Souvenirs, Booking and Contact.

## Local setup
1. Create and activate a Python virtual environment.
2. Install packages: `pip install -r requirements.txt`.
3. Set `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`.
4. Run `python manage.py migrate`.
5. Create an admin account: `python manage.py createsuperuser`.
6. Run `python manage.py runserver`.

Open `/` for the website and `/admin/` to manage homepage content, services, souvenirs, bookings and contact messages. Booking and contact submissions are stored in the database.

## Railway
Connect the repository to Railway and deploy branch `django-backend-bootstrap`. Add a PostgreSQL service and set `DATABASE_URL`, `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS` (your Railway hostname), and `DJANGO_CSRF_TRUSTED_ORIGINS` (the https origin). Start command:
`python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

Cloudinary is planned but not yet integrated. Add its credentials as Railway environment variables before enabling uploads. Do not commit credentials. This branch has not been deployed or tested against your live Railway service yet.
