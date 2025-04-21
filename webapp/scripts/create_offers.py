import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()

# Now import your models
from properties.models import Offer


def create_sample_offers():
    # clear existing
    Offer.objects.all().delete()

    offers = [
        Offer(
            name="Modern Loft",
            beds_count=1,
            baths_count=1,
            area=50,
            price=650000.00,
            description="""
<h2>Urban Elegance Meets Industrial Chic</h2>
<p>
  Step into <strong>The Foundry Loft</strong> — a striking blend of modern minimalism and historic character nestled in the heart of the city.
  With soaring <strong>14-foot ceilings</strong>, exposed brick walls, and floor-to-ceiling windows that flood the space with natural light,
  this one-of-a-kind loft offers a perfect harmony of style and function.
</p>

<p>
  Whether you're hosting a wine night under statement pendant lighting or sipping your morning coffee on the private balcony with skyline views,
  every corner is designed to inspire. Featuring a <strong>chef’s kitchen</strong> with quartz countertops, <em>spa-inspired bathroom</em>,
  and smart home upgrades throughout, <strong>The Foundry Loft</strong> is more than a home — it’s a lifestyle.
</p>

<p><em><strong>Live bold. Live refined. Live loft.</strong></em></p>
            """,
            image='modern-loft.jpeg',
            slug="modern-loft"
        ),
        Offer(
            name="Family House",
            beds_count=3,
            baths_count=2,
            area=150,
            price=1450000.00,
            description="Perfect house for a family.",
            slug="family-house"
        ),
        Offer(
            name="Modern Family Home",
            beds_count=3,
            baths_count=2,
            area=280,
            price=4500000.00,
            description="Perfect house for a family.",
            slug="modern-family-house"
        ),
        Offer(
            name="Modern Apartment",
            beds_count=2,
            baths_count=1,
            area=80,
            price=350000.00,
            description="Stylish city apartment with a great view.",
            slug="modern-apartment"
        ),
        Offer(
            name="Luxury Villa",
            beds_count=5,
            baths_count=4,
            area=300,
            price=3200000.00,
            description="Exquisite villa with private pool and garden.",
            slug="luxury-villa"
        ),
        Offer(
            name="City Apartment",
            beds_count=2,
            baths_count=1,
            area=75,
            price=850000.00,
            description="Stylish apartment in the heart of the city.",
            slug="city-apartment"
        ),
        Offer(
            name="Luxury Villa",
            beds_count=5,
            baths_count=4,
            area=300,
            price=3200000.00,
            description="Spacious villa with private pool and garden.",
            slug="luxury-villa"
        ),
        Offer(
            name="Cozy Studio",
            beds_count=1,
            baths_count=1,
            area=30,
            price=350000.00,
            description="Compact studio ideal for city living.",
            slug="cozy-studio"
        ),
        Offer(
            name="Suburban Cottage",
            beds_count=2,
            baths_count=1,
            area=90,
            price=950000.00,
            description="Charming cottage located in a quiet suburban area.",
            slug="suburban-cottage"
        ),
        Offer(
            name="Penthouse Suite",
            beds_count=3,
            baths_count=3,
            area=200,
            price=2500000.00,
            description="Exclusive penthouse with panoramic city views.",
            slug="penthouse-suite"
        )
    ]

    # Bulk create the offers
    created = Offer.objects.bulk_create(offers)
    print(f"Created {len(created)} offers successfully!")


if __name__ == "__main__":
    create_sample_offers()
