from app.main import SessionLocal, User, get_password_hash, Role

def seed_admin():
    db = SessionLocal()
    admin_exists = db.query(User).filter(User.username == "admin").first()
    if not admin_exists:
        admin = User(
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            role=Role.ADMIN
        )
        db.add(admin)
        db.commit()
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")
    db.close()

if __name__ == "__main__":
    seed_admin()
