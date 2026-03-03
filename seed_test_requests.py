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

test_data = [
    {"product": "لاب توب ديل", "name": "أحمد محمد", "days_ago": 10, "status": RequestStatus.APPROVED},
    {"product": "شاشة سامسونج", "name": "سارة علي", "days_ago": 5, "status": RequestStatus.PENDING},
    {"product": "طابعة ليزر", "name": "خالد فهد", "days_ago": 2, "status": RequestStatus.REJECTED},
    {"product": "ماوس لاسلكي", "name": "منيرة عبد الله", "days_ago": 1, "status": RequestStatus.APPROVED},
    {"product": "لوحة مفاتيح ميكانيكية", "name": "يوسف إبراهيم", "days_ago": 0, "status": RequestStatus.PENDING},
]

for i, data in enumerate(test_data):
    order_num = f"{next_id + i:02d}"
    created_at = datetime.now() - timedelta(days=data["days_ago"])
    
    new_req = PurchaseRequest(
        order_number=order_num,
        requester_name=data["name"],
        product_name=data["product"],
        quantity=random.randint(1, 10),
        image_path="/static/uploads/b3ee454d-d3a4-4a59-8b0e-c164103c07f0.webp",
        status=data["status"],
        created_at=created_at,
        user_id=user.id
    )
    db.add(new_req)

db.commit()
print(f"Successfully added 5 test requests for user {user.username}")
db.close()
