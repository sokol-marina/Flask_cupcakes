from app import app
from models import db, Cupcake

def seed_data():
    with app.app_context():
        # Create all tables
        db.drop_all()
        db.create_all()

        # Clear existing data
        Cupcake.query.delete()

        # Add sample data
        cupcake1 = Cupcake(flavor="Chocolate", size="Medium", rating=4.5)
        cupcake2 = Cupcake(flavor="Vanilla", size="Large", rating=4.0)
        cupcake3 = Cupcake(flavor="Red Velvet", size="Small", rating=4.8)

        # Add cupcakes to the session
        db.session.add_all([cupcake1, cupcake2, cupcake3])

        # Commit to save the cupcakes in the database
        db.session.commit()

if __name__ == "__main__":
    seed_data()
    print("Seed data added successfully!")
