from django.core.management.base import BaseCommand
import cloudinary
import cloudinary.api
import cloudinary.uploader
import requests

# Поддерживаемые расширения изображений
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif")

class Command(BaseCommand):
    help = "Convert all raw image files in Cloudinary to image resources"

    def handle(self, *args, **options):
        self.stdout.write("🔍 Fetching raw resources from Cloudinary...")

        next_cursor = None
        total_converted = 0
        total_found = 0

        while True:
            params = {"resource_type": "raw", "max_results": 500}
            if next_cursor:
                params["next_cursor"] = next_cursor

            result = cloudinary.api.resources(**params)
            raws = result.get("resources", [])
            total_found += len(raws)
            self.stdout.write(f"Found {len(raws)} raw files in this batch")

            # Фильтруем только изображения
            image_like = [
                f for f in raws
                if f["public_id"].lower().endswith(IMAGE_EXTENSIONS)
            ]
            self.stdout.write(f"🖼 {len(image_like)} image-like raw files in this batch")

            for f in image_like:
                public_id = f["public_id"]
                raw_url = f["secure_url"]
                try:
                    self.stdout.write(f"⬇ Downloading {public_id}")
                    response = requests.get(raw_url, timeout=30)
                    response.raise_for_status()

                    upload = cloudinary.uploader.upload(
                        response.content,
                        resource_type="image",  # 🔥 Конвертация в image
                        public_id=public_id,    # сохраняем имя
                        overwrite=True
                    )

                    total_converted += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Converted: {upload['secure_url']}")
                    )

                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"❌ Failed {public_id}: {e}")
                    )

            next_cursor = result.get("next_cursor")
            if not next_cursor:
                break

        self.stdout.write(self.style.SUCCESS(
            f"🎉 Done! Found {total_found} raw files, converted {total_converted} images."
        ))
