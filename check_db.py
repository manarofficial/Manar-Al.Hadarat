from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///./purchase_system.db")
inspector = inspect(engine)
columns = [col['name'] for col in inspector.get_columns('requests')]
print(f"Columns in 'requests' table: {columns}")
