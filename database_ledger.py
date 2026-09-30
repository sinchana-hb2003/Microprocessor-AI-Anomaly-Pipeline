import os
import sqlite3
import pandas as pd

print("🗄️ Starting Phase 3: Building Relational SQL Database Ledger...")

# 1. Initialize our local SQLite database infrastructure file
db_name = "semiconductor_factory.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# 2. Build our database table layout with explicit data schemas
cursor.execute("""
CREATE TABLE IF NOT EXISTS chip_inventory_logs (
    chip_uuid TEXT PRIMARY KEY,
    file_name TEXT NOT NULL,
    storage_path TEXT NOT NULL,
    condition_class TEXT NOT NULL,
    is_defective_flag INTEGER NOT NULL
)
""")
conn.commit()
print(f"✅ Success: Relational table schema created inside '{db_name}'.")

# 3. Use Pandas to crawl your newly populated folders and index the data
subfolders = ["Normal_chips", "Defective_chips"]
registered_records = []

for class_label, folder_name in enumerate(subfolders):
    if os.path.exists(folder_name):
        for img_file in os.listdir(folder_name):
            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                registered_records.append({
                    "chip_uuid": f"CHIP-{folder_name[:3].upper()}-{len(registered_records)+1:04d}",
                    "file_name": img_file,
                    "storage_path": os.path.join(folder_name, img_file),
                    "condition_class": folder_name,
                    "is_defective_flag": class_label  # 0 for Normal, 1 for Defective
                })

# Pack rows into a clean Pandas DataFrame
df_asset_registry = pd.DataFrame(registered_records)

# 4. Stream the data frame matrix records directly into the SQL Table
df_asset_registry.to_sql("chip_inventory_logs", conn, if_exists="replace", index=False)
print(f"⚡ Ingested {len(df_asset_registry)} row logs into the SQL database ledger table.")

# 5. Run the Premium AI Audit Query
# This queries the database to grab ONLY defective files to form our focused AI training targets
print("\n🔍 Running SQL Compliance Audit Query...")
audit_query = """
SELECT chip_uuid, file_name, condition_class 
FROM chip_inventory_logs 
WHERE is_defective_flag = 1 
LIMIT 5;
"""

df_failed_chips = pd.read_sql_query(audit_query, conn)
print("\n--- CRITICAL HARDWARE FAULTS ISOLATED BY SQL DATABASE FOR AI CORES ---")
print(df_failed_chips)

# Safely close our database connection pipelines
conn.close()
print("\n🎉 Database tracking infrastructure setup complete!")
