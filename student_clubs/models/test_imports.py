import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

# Now import the model
from student_clubs.models import StudentProfile

print("Successfully imported StudentProfile!")
print(f"Model name: {StudentProfile._meta.verbose_name}")

# Count instances
count = StudentProfile.objects.count()
print(f"Found {count} instances")
