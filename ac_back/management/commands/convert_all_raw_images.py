# core/management/commands/convert_all_raw_images.py
import cloudinary
import cloudinary.api
import cloudinary.uploader
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Convert all old raw images in Cloudinary to image resource_type"

    IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "webp"]

    def handle(self, *args, **options):
        self.stdout.write("🔍 Fetching all raw files from Cloudinary...")
        next_cursor = None
        total_converted = 0

        while True:
            try:
                res = cloudinary.api.resources(
                    type="upload",          # важно для новых версий API
                    resource_type="raw",    # ищем raw-файлы
                    max_results=500,
                    next_cursor=next_cursor
                )
            except cloudinary.exceptions.Error as e:
                self.stderr.write(f"❌ Cloudinary API error: {e}")
                break

            resources = res.get("resources", [])
            if not resources:
                break

            for r in resources:
                public_id = r["public_id"]
                file_type = r.get("format", "").lower()

                # конвертируем только изображения
                if file_type in self.IMAGE_EXTENSIONS:
                    url = r.get("url") or r.get("secure_url")
                    self.stdout.write(f"⬇ Converting raw image: {public_id}")
                    try:
                        cloudinary.uploader.upload(
                            url,
                            resource_type="image",
                            public_id=public_id,
                            overwrite=True
                        )
                        self.stdout.write(f"✅ Converted: {public_id}")
                        total_converted += 1
                    except cloudinary.exceptions.Error as e:
                        self.stderr.write(f"❌ Failed to convert {public_id}: {e}")

            next_cursor = res.get("next_cursor")
            if not next_cursor:
                break

        self.stdout.write(f"🎉 Done! Converted {total_converted} images.")
