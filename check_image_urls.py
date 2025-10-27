import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')
django.setup()

from news.models import News
from banner.models import BannerSlide

print("=" * 60)
print("ПРОВЕРКА URL ИЗОБРАЖЕНИЙ")
print("=" * 60)

# Проверяем новости
news = News.objects.first()
if news and news.image:
    print(f"\n📰 News Image URL:")
    print(f"   {news.image.url}")
else:
    print("\n⚠️  Нет новостей с изображениями")

# Проверяем баннеры
banner = BannerSlide.objects.first()
if banner and banner.image:
    print(f"\n🖼️  Banner Image URL:")
    print(f"   {banner.image.url}")
else:
    print("\n⚠️  Нет баннеров с изображениями")

print("\n" + "=" * 60)
