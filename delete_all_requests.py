from app.main import SessionLocal, PurchaseRequest

def delete_all_requests():
    db = SessionLocal()
    try:
        num_deleted = db.query(PurchaseRequest).delete()
        db.commit()
        print(f"Successfully deleted {num_deleted} requests.")
    except Exception as e:
        db.rollback()
        print(f"Error deleting requests: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    delete_all_requests()
