initial read me

## Cloudinary media storage (images and videos)

Uploads made in `/admin` (promo banners, release artwork, souvenirs, feature videos and posters) are stored in Cloudinary when credentials are present. Without them the site still runs and falls back to local disk, which is lost on every Railway redeploy (a `core.W001` warning appears in `manage.py check --deploy`).

Set ONE of these in the environment (never commit values; see `.env.example`):

1. `CLOUDINARY_URL` = `cloudinary://API_KEY:API_SECRET@CLOUD_NAME` (Cloudinary Console > API Keys), or
2. `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY` and `CLOUDINARY_API_SECRET` together.

A half-set configuration is reported as error `core.E001` instead of crashing at import.

Railway: add the variable in the service's Variables tab for the environment you are deploying (staging first). Use a sealed variable. Then redeploy.

Verify after deploy: upload a promo banner and a feature video in `/admin`; the file URLs should start with `https://res.cloudinary.com/<cloud_name>/image/upload/` and `.../video/upload/`.

Notes: videos use Cloudinary's `video` resource type (`core/storage.py`). Existing files already on local disk are not migrated; re-upload them.

Run checks: `python manage.py test` and `python manage.py check --deploy`.
