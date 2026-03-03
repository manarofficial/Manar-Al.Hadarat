from app.main import SessionLocal, User, get_password_hash

def change_admin_password(new_password):
    db = SessionLocal()
    admin = db.query(User).filter(User.username == "admin").first()
    if admin:
        admin.hashed_password = get_password_hash(new_password)
        db.commit()
        print(f"Password for user 'admin' changed successfully.")
    else:
        print("User 'admin' not found.")
    db.close()

if __name__ == "__main__":
    change_admin_password("P@fasbook")
