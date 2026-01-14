from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction
from django.db.models import TextField, CharField, FileField, ImageField, Q

class Command(BaseCommand):
    help = "Replace /raw/upload/ → /image/upload/ in all fields using ORM"

    def handle(self, *args, **options):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("🔄 Searching and replacing /raw/upload/ → /image/upload/\n")
        
        total_replaced = 0
        found_models = []
        
        # Get all models
        for model in apps.get_models():
            app_label = model._meta.app_label
            model_name = model._meta.model_name
            
            # Get all text/file fields
            text_fields = []
            for field in model._meta.get_fields():
                if isinstance(field, (TextField, CharField, FileField, ImageField)):
                    text_fields.append(field.name)
            
            if not text_fields:
                continue
            
            try:
                # Build Q object for searching
                q_objects = Q()
                for field in text_fields:
                    q_objects |= Q(**{f"{field}__contains": "/raw/upload/"})
                
                qs = model.objects.filter(q_objects)
                
                if qs.count() > 0:
                    found_models.append((model_name, qs.count()))
                    self.stdout.write(
                        self.style.WARNING(
                            f"⚠️  Found {qs.count()} records in {model_name}"
                        )
                    )
                    
                    with transaction.atomic():
                        for obj in qs:
                            for field in text_fields:
                                original = getattr(obj, field, None)
                                if original and isinstance(original, str) and '/raw/upload/' in original:
                                    fixed = original.replace('/raw/upload/', '/image/upload/')
                                    setattr(obj, field, fixed)
                            obj.save()
                            total_replaced += 1
                            self.stdout.write(
                                self.style.SUCCESS(f"  ✔ Updated {model_name} id={obj.id}")
                            )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error in {model_name}: {e}")
                )
        
        self.stdout.write("\n" + "="*60)
        if found_models:
            self.stdout.write(self.style.SUCCESS(f"✓ Done! Replaced in {len(found_models)} models:"))
            for model_name, count in found_models:
                self.stdout.write(f"  • {model_name}: {count} records")
            self.stdout.write(f"\nTotal records updated: {total_replaced}")
        else:
            self.stdout.write(self.style.SUCCESS("✓ No /raw/upload/ URLs found!"))
        self.stdout.write("="*60 + "\n")
