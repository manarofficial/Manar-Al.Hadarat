from app.main import SessionLocal, PurchaseRequest
db = SessionLocal()
reqs = db.query(PurchaseRequest).all()
for r in reqs:
    print(f"Order: {r.order_number}, Name: {r.requester_name!r}, Type: {type(r.requester_name)}")
db.close()
