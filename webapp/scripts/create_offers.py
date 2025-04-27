import os
import sys
import django


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Adjust as needed
sys.path.insert(0, project_root)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()

from properties.models import Offer

def create_sample_offers():
    # clear existing
    Offer.objects.all().delete()

    offers = [
        Offer(
            name="Modern Family Home",
            beds_count=3,
            baths_count=2,
            area=150,
            price=1450000.00,
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
            image='img/house2.jpg',
            slug="modern-family-home"
        ),
        Offer(
            name="Scandinavian Apartment",
            beds_count=2,
            baths_count=1,
            area=90,
            price=250000.00,
            description="""
            <h2>Scandinavian Serenity Meets Sleek Sophistication</h2>
<p>
  Welcome to <strong>The Nord Haus</strong> — a luminous retreat where clean lines, natural textures, and timeless design create an atmosphere of effortless calm.
  Bathed in soft, golden light through <strong>panoramic windows</strong>, this elegant space embraces the essence of Scandinavian living with its open floor plan,
  pale oak floors, and curated minimalist details.
</p>

<p>
  Whether you're gathering for a cozy dinner under a modern glass chandelier or savoring a quiet morning by the fireplace nook,
  every inch of <strong>The Nord Haus</strong> feels intentional and inspiring. Featuring a <strong>bespoke kitchen</strong> with marble accents,
  an <em>organic spa bathroom</em> with heated floors, and integrated smart features, this apartment isn’t just a place to live — it’s a sanctuary.
</p>

<p><em><strong>Live light. Live pure. Live Nord.</strong></em></p>

            """,
            image='img/house1.jpg',
            slug="scandinavian-apartment"
        ),
        Offer(
            name="Cozy Country House",
            beds_count=2,
            baths_count=1,
            area=200,
            price=410000.00,
            description="""
            <h2>Rustic Charm Meets Modern Comfort</h2>
<p>
  Welcome to <strong>The Willow Cottage</strong> — a warm embrace of countryside beauty and contemporary ease tucked away in rolling meadows.
  With <strong>vaulted beam ceilings</strong>, wide-plank wood floors, and sun-dappled rooms framed by charming French doors,
  every detail invites you to slow down and savor the simple joys of home.
</p>

<p>
  Whether you're sharing stories by the stone fireplace or enjoying a lazy afternoon on the wraparound porch,
  <strong>The Willow Cottage</strong> is made for moments that linger. Featuring a <strong>gourmet farmhouse kitchen</strong> with butcher block counters,
  an <em>artisan-crafted bathroom</em> with a vintage clawfoot tub, and thoughtful modern updates throughout, this home is where nostalgia meets now.
</p>

<p><em><strong>Live warmly. Live simply. Live country.</strong></em></p>
            """,
            image='img/country-house.jpg',
            slug="cozy-country-house"
        ),
        Offer(
            name="Minimalist Villa",
            beds_count=5,
            baths_count=4,
            area=300,
            price=680000.00,
            description="Exquisite villa with private pool and garden.",
            image='img/decor-hero.jpg',
            slug="minimalist-villa"
        ),
        Offer(
            name="Urban Loft",
            beds_count=2,
            baths_count=2,
            area=110,
            price=290000.00,
            description="Stylish apartment in the heart of the city.",
            image='img/house.jpg',
            slug="urban-loft"
        ),
        Offer(
            name="Elegant Penthouse",
            beds_count=5,
            baths_count=4,
            area=300,
            price=540000.00,
            description="Spacious villa with private pool and garden.",
            image='img/modern-loft1.jpeg',
            slug="elegant-penthouse"
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
        )
    ]

    # Bulk create the offers
    created = Offer.objects.bulk_create(offers)
    print(f"Created {len(created)} offers successfully!")


if __name__ == "__main__":
    create_sample_offers()
