import os
import shutil

# 1. Map the exact path visible in your VS Code sidebar tree
source_base_dir = "Semiconductor wafer detect/WM811k_Dataset"

# 2. Match your empty destination folders
target_normal_dir = "Normal_chips"
target_defect_dir = "Defective_chips"

# 3. Use the exact spelling of the subfolders visible in your screenshot
defect_folders = ["Center", "Donut", "Edge Local", "Edge Ring", "Local", "near full", "random", "Scratch"]
normal_folder = "none"

print("⚡ Starting automated wafer chip sorting operation...")
moved_normal = 0
moved_defective = 0

# Ensure our target folders exist locally
os.makedirs(target_normal_dir, exist_ok=True)
os.makedirs(target_defect_dir, exist_ok=True)

# --- SECTION 1: Populate Normal Chips ---
src_normal_path = os.path.join(source_base_dir, normal_folder)
if os.path.exists(src_normal_path):
    # Take the first 100 clean chips to keep our AI training lean and fast
    all_normal_files = [f for f in os.listdir(src_normal_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for img_file in all_normal_files[:100]:
        shutil.copy(os.path.join(src_normal_path, img_file), os.path.join(target_normal_dir, img_file))
        moved_normal += 1
else:
    print(f"❌ Missing expected normal path source: {src_normal_path}")

# --- SECTION 2: Populate Defective Chips ---
for folder in defect_folders:
    src_defect_path = os.path.join(source_base_dir, folder)
    if os.path.exists(src_defect_path):
        # Collect up to 15 real samples from each type of hardware fault
        all_defect_files = [f for f in os.listdir(src_defect_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        for img_file in all_defect_files[:15]:
            shutil.copy(os.path.join(src_defect_path, img_file), os.path.join(target_defect_dir, img_file))
            moved_defective += 1
    else:
        print(f"⚠️ Warning: Could not locate directory: {src_defect_path}")

print("\n📦 Automated Dataset Setup Complete!")
print(f"-> Successfully copied {moved_normal} clean wafer scans into '{target_normal_dir}/'")
print(f"-> Successfully copied {moved_defective} fault anomaly maps into '{target_defect_dir}/'")
print("🎉 Your local folders are now populated and ready for your deep learning pipeline!")
