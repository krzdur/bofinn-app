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
            description="""
<h2>Serene Living in Scandinavian Harmony</h2>
<p>
  Welcome to the <strong>Minimalist Villa</strong> — a tranquil retreat where clean architectural lines, soft textures,
  and natural light come together in perfect balance. Surrounded by gentle greenery and designed with intentional simplicity,
  this home invites you to slow down and reconnect.
</p>
<p>
  Featuring <strong>open-concept living spaces</strong>, floor-to-ceiling windows, and a seamless indoor-outdoor flow,
  the villa offers a sense of effortless spaciousness. A <strong>wood-accented kitchen</strong> with matte finishes,
  <em>spa-like bathrooms</em>, and cozy reading nooks make it both functional and restorative.
</p>
<p>
  Whether you're enjoying a morning coffee on the sun-washed patio or hosting intimate dinners under soft pendant lighting,
  every corner whispers calm. <strong>Minimalist Villa</strong> is more than a place to live — it’s a space to breathe.
</p>
<p><em><strong>Live simply. Live fully. Live grounded.</strong></em></p>
            """,
            image='img/decor-hero.jpg',
            slug="minimalist-villa"
        ),
        Offer(
            name="Urban Loft",
            beds_count=2,
            baths_count=2,
            area=110,
            price=290000.00,
            description="""
<h2>Industrial Soul with City Sophistication</h2>
<p>
  Discover the bold charm of the <strong>Urban Loft</strong> — where exposed concrete, steel beams,
  and natural textures meet downtown energy. Nestled in a reimagined factory building, this loft captures the raw
  authenticity of urban living while offering refined, modern comfort.
</p>
<p>
  Enjoy <strong>16-foot ceilings</strong>, massive industrial-style windows, and polished concrete floors.
  The open floor plan boasts a <strong>designer kitchen</strong> with dark quartz countertops, a <em>glass-enclosed mezzanine bedroom</em>,
  and smart lighting to set the mood for any moment.
</p>
<p>
  Whether you’re crafting ideas in the work-from-home alcove or hosting friends in the dramatic living space,
  the <strong>Urban Loft</strong> delivers inspiration at every turn.
</p>
<p><em><strong>Live raw. Live real. Live downtown.</strong></em></p>

            """,
            image='img/house.jpg',
            slug="urban-loft"
        ),
        Offer(
            name="Elegant Penthouse",
            beds_count=5,
            baths_count=4,
            area=300,
            price=540000.00,
            description="""
<h2>Skyline Living with Timeless Grace</h2>
<p>
  Introducing the <strong>Elegant Penthouse</strong> — a crown jewel of modern refinement perched high above the city.
  With expansive terraces, panoramic skyline views, and sophisticated finishes throughout, this is high-rise living at its most graceful.
</p>
<p>
  Step into a <strong>sun-drenched great room</strong> with marble floors, custom built-ins, and French doors that open
  to a private rooftop oasis. The <strong>chef’s kitchen</strong> features integrated appliances and golden brass fixtures,
  while the <em>primary suite</em> includes a walk-in dressing room and a deep soaking tub framed by city lights.
</p>
<p>
  Ideal for elegant entertaining or serene solitude, the <strong>Elegant Penthouse</strong> is a space where luxury and
  tranquility live side by side.
</p>
<p><em><strong>Live elevated. Live refined. Live above it all.</strong></em></p>

            """,
            image='img/modern-loft1.jpeg',
            slug="elegant-penthouse"
        )
    ]

    # Bulk create the offers
    created = Offer.objects.bulk_create(offers)
    print(f"Created {len(created)} offers successfully!")


if __name__ == "__main__":
    create_sample_offers()
