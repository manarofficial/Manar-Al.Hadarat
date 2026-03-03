from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import PurchaseRequest, User, RequestStatus
from datetime import datetime, timedelta
import random

SQLALCHEMY_DATABASE_URL = "sqlite:///./purchase_system.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Get a user
user = db.query(User).filter(User.username == 'batman').first()
if not user:
    user = db.query(User).first()

if not user:
    print("No user found to assign requests to.")
    exit()

# Get last order number
last_request = db.query(PurchaseRequest).order_by(PurchaseRequest.id.desc()).first()
next_id = (last_request.id + 1) if last_request else 1

# Add 5 more requests with different dates
test_data = [
    {"product": "طابعة ملوّنة إتش بي", "name": "فيصل محمد", "days_ago": 15, "status": RequestStatus.APPROVED},
    {"product": "مكيف سبليت جنرال", "name": "تركي الحربي", "days_ago": 8, "status": RequestStatus.PENDING},
    {"product": "جهاز آيباد برو", "name": "مشعل القحطاني", "days_ago": 3, "status": RequestStatus.APPROVED},
    {"product": "سماعات آبل", "name": "نواف الشمري", "days_ago": 1, "status": RequestStatus.APPROVED},
    {"product": "هاردسك خارجي 2 تيرا", "name": "سلطان العتيبي", "days_ago": 0, "status": RequestStatus.PENDING},
]

for i, data in enumerate(test_data):
    order_num = f"{next_id + i:02d}"
    created_at = datetime.now() - timedelta(days=data["days_ago"])
    
    new_req = PurchaseRequest(
        order_number=order_num,
        requester_name=data["name"],
        product_name=data["product"],
        quantity=random.randint(1, 5),
        image_path="/static/uploads/b3ee454d-d3a4-4a59-8b0e-c164103c07f0.webp", # Reusing existing image
        status=data["status"],
        created_at=created_at,
        user_id=user.id
    )
    db.add(new_req)

db.commit()
print(f"Successfully added 5 MULTI-DATE test requests for user {user.username}")
db.close()
