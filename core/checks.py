from django.conf import settings
from django.core.checks import Error, Warning, register


@register(deploy=True)
def cloudinary_config(app_configs, **kwargs):
    if getattr(settings, "CLOUDINARY_PARTIAL", False):
        return [Error(
            "Cloudinary is only partly configured.",
            hint="Set a valid CLOUDINARY_URL (cloudinary://API_KEY:API_SECRET@CLOUD_NAME) or all of "
                 "CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET.",
            id="core.E001")]
    if not getattr(settings, "USE_CLOUDINARY", False) and not settings.DEBUG:
        return [Warning(
            "Cloudinary credentials are not set; uploaded images and videos are stored on local disk and "
            "will be lost on redeploy.",
            hint="Add the Cloudinary variables in Railway (see .env.example).",
            id="core.W001")]
    return []
