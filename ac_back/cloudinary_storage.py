from cloudinary_storage.storage import MediaCloudinaryStorage

class RawMediaCloudinaryStorage(MediaCloudinaryStorage):
    """Хранилище Cloudinary для PDF и других raw файлов"""
    def __init__(self, *args, **kwargs):
        kwargs['resource_type'] = 'raw'  # <--- важно для PDF, docx и др.
        super().__init__(*args, **kwargs)
    
