# Duke Vadis Official Website
Django artist website with editable songs, gallery media, booking enquiries and Django admin.

## Local setup
Install dependencies with `pip install -r requirements.txt`, then run `python manage.py migrate`, `python manage.py createsuperuser`, and `python manage.py runserver`. Visit `/admin/` to manage content.

## Railway
Set a strong `SECRET_KEY`; attach a Railway PostgreSQL database to provide `DATABASE_URL`; set `CLOUDINARY_URL` to the Cloudinary connection string; configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for the deployed domain. Run migrations before serving traffic. Upload the supplied artist portrait and promotional poster to Cloudinary, then add them through the admin/gallery. Never commit secrets.
