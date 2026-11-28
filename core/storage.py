from django.conf import settings
from django.core.files.storage import default_storage


def video_storage():
    """Videos need Cloudinary's "video" resource type; the default storage uploads as "image".

    Without Cloudinary credentials this returns the default (local disk) storage.
    """
    if getattr(settings, "USE_CLOUDINARY", False):
        from cloudinary_storage.storage import VideoMediaCloudinaryStorage
        return VideoMediaCloudinaryStorage()
    return default_storage
