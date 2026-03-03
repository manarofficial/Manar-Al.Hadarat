from app.main import SessionLocal, PurchaseRequest, User, Role
import random

def seed_50_requests():
    db = SessionLocal()
    
    # Get admin user to associate requests with
    admin = db.query(User).filter(User.role == Role.ADMIN).first()
    if not admin:
        print("Error: No admin user found. Please run seed_admin.py first.")
        db.close()
        return

    # Sample products and names for randomization
    products = [
        "جهاز كمبيوتر محمول", "طابعة مكتبية", "شاشة 27 بوصة", "لوحة مفاتيح لاسلكية",
        "فارة ضوئية", "كرسي مكتب مريح", "طاولة اجتماعات", "أحبار طابعة",
        "ورق A4", "كاميرا مراقبة", "جهاز عرض (بروجكتور)", "سماعات رأس"
    ]
    requesters = [
        "أحمد محمد", "سارة خالد", "فهد عبد الله", "نورة علي", 
        "محمد حسن", "ريم إبراهيم", "ياسر محمود", "ليلى يوسف"
    ]

    # Get an existing image from static/uploads to reuse
    # In a real scenario, we'd copy a file, but for seeding 50, let's just point to an existing one
    # if it exists, otherwise use a placeholder string.
    sample_image = "/static/uploads/b3ee454d-d3a4-4a59-8b0e-c164103c07f0.webp"

    print(f"Seeding 50 requests for user: {admin.username}")

    for i in range(1, 51):
        # Generate sequential order number based on current count in DB
        last_request = db.query(PurchaseRequest).order_by(PurchaseRequest.id.desc()).first()
        next_id = (last_request.id + 1) if last_request else 1
        order_number = f"{next_id:02d}"

        new_request = PurchaseRequest(
            order_number=order_number,
            requester_name=random.choice(requesters),
            product_name=random.choice(products),
            quantity=random.randint(1, 10),
            image_path=sample_image,
            user_id=admin.id,
            status="pending"
        )
        db.add(new_request)
        db.commit()
        print(f"Created request {i}/50: Order #{order_number}")

    db.close()
    print("Successfully created 50 requests.")

if __name__ == "__main__":
    seed_50_requests()
