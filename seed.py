from app import app, db, Landmark, Cuisine, Event

# Use Flask application context
with app.app_context():
    # Insert sample landmarks in Bengaluru
    db.session.add(Landmark(name="Bangalore Palace", description="Historic royal palace inspired by Tudor architecture."))
    db.session.add(Landmark(name="Lalbagh Botanical Garden", description="Famous botanical garden with diverse flora."))
    db.session.add(Landmark(name="Vidhana Soudha", description="Iconic government building known for its grand architecture."))

    # Insert sample cuisines in Bengaluru
    db.session.add(Cuisine(name="Masala Dosa", specialty="Popular South Indian crispy dosa with spicy potato filling."))
    db.session.add(Cuisine(name="Bisi Bele Bath", specialty="Traditional Karnataka dish made with rice, lentils, and spices."))
    db.session.add(Cuisine(name="Mysore Pak", specialty="Famous sweet from Karnataka made of ghee, sugar, and gram flour."))

    # Insert sample events in Bengaluru
    db.session.add(Event(name="Bangalore Literature Festival", date="2025-08-10", location="Lalit Ashok Hotel"))
    db.session.add(Event(name="Tech Summit", date="2025-11-15", location="Bangalore International Exhibition Centre"))
    db.session.add(Event(name="Karaga Festival", date="2025-04-15", location="Dharmaraya Swamy Temple"))
    db.session.add(Event(name="Bangalore Open Air", date="2025-07-05", location="Royal Orchid Resort"))

    # Commit changes to the database
    db.session.commit()
 
