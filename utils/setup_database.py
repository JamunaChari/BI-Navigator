import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))


from services.database_service import DatabaseService


database = DatabaseService()

database.execute_script("database/schema.sql")
database.execute_script("database/seed_data.sql")

print("Database created successfully!")