from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction, connection
from django.db.models import TextField, CharField, FileField, ImageField

class Command(BaseCommand):
    help = "Mass replace /raw/upload/ → /image/upload/ in all Cloudinary URLs across all models"

    def get_text_fields(self, model):
        """Get all text-type fields from a model (including media fields)"""
        text_fields = []
        for field in model._meta.get_fields():
            # Include text fields and media fields
            if isinstance(field, (TextField, CharField, FileField, ImageField)):
                text_fields.append(field.name)
        return text_fields

    def handle(self, *args, **options):
        total_replacements = 0
        total_fields_updated = 0

        self.stdout.write("\n" + "="*60)
        self.stdout.write("🔄 Searching for /raw/upload/ URLs in database...\n")

        # Get all models from all apps
        for model in apps.get_models():
            app_label = model._meta.app_label
            model_name = model._meta.model_name
            table_name = model._meta.db_table
            
            # Get text fields for this model
            text_fields = self.get_text_fields(model)
            
            if not text_fields:
                continue
            
            try:
                qs = model.objects.all()
                if qs.count() == 0:
                    continue
                
                self.stdout.write(
                    f"Processing {app_label}.{model_name} ({qs.count()} records, {len(text_fields)} text fields)..."
                )

                with transaction.atomic():
                    for obj in qs:
                        updated = False
                        for field in text_fields:
                            try:
                                original = getattr(obj, field, None)
                                if original and isinstance(original, str) and '/raw/upload/' in original:
                                    fixed = original.replace('/raw/upload/', '/image/upload/')
                                    setattr(obj, field, fixed)
                                    updated = True
                                    total_fields_updated += 1
                            except Exception as e:
                                self.stdout.write(
                                    self.style.WARNING(f"  ⚠ Error processing {model_name}.{field} id={obj.id}: {e}")
                                )
                        
                        if updated:
                            try:
                                obj.save()
                                total_replacements += 1
                                self.stdout.write(
                                    self.style.SUCCESS(f"  ✔ Updated {model_name} id={obj.id}")
                                )
                            except Exception as e:
                                self.stdout.write(
                                    self.style.ERROR(f"  ✗ Failed to save {model_name} id={obj.id}: {e}")
                                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error processing {app_label}.{model_name}: {e}")
                )

        self.stdout.write("\n" + "="*60)
        self.stdout.write(self.style.SUCCESS(
            f"✓ Done!\n"
            f"  • Records updated: {total_replacements}\n"
            f"  • Fields fixed: {total_fields_updated}"
        ))
        self.stdout.write("="*60)
