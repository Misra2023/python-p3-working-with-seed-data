# lib/seed.py
from models import Game, session
from faker import Faker
import random

# Add a console message so we can see output when the seed file runs
print("Seeding games...")

fake = Faker()

# Clear old data
session.query(Game).delete()
session.commit()

# Generate and add 50 random game records
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

session.add_all(games)
session.commit()

print("Seeding complete!")
