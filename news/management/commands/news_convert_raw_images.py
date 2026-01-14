# news/management/commands/news_convert_raw_to_image.py
import cloudinary
import cloudinary.api
import cloudinary.uploader
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Convert old raw news images to image resource_type in Cloudinary"

    def handle(self, *args, **options):
        self.stdout.write("🔍 Fetching raw news files from Cloudinary...")
        next_cursor = None
        total_converted = 0

        while True:
            res = cloudinary.api.resources(
                type="upload",          # важно!
                resource_type="raw",    # ищем старые raw
                prefix="media/news",
                max_results=500,
                next_cursor=next_cursor
            )

            resources = res.get("resources", [])
            if not resources:
                break

            for r in resources:
                public_id = r["public_id"]
                file_type = r.get("format", "").lower()
                if file_type in ["jpg", "jpeg", "png", "webp"]:
                    url = r.get("url") or r.get("secure_url")
                    self.stdout.write(f"⬇ Converting raw image: {public_id}")
                    cloudinary.uploader.upload(
                        url,
                        resource_type="image",
                        public_id=public_id,
                        overwrite=True
                    )
                    self.stdout.write(f"✅ Converted: {public_id}")
                    total_converted += 1

            next_cursor = res.get("next_cursor")
            if not next_cursor:
                break

        self.stdout.write(f"🎉 Done! Converted {total_converted} news images.")
