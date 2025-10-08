import os
import shutil

# Set paths
src_folder = "images"
dest_folder = "face_dataset"

# Create destination folders
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

for filename in os.listdir(src_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        name = filename.split('_')[0].lower()  # assumes format like akash_1.jpg
        person_folder = os.path.join(dest_folder, name)
        if not os.path.exists(person_folder):
            os.makedirs(person_folder)
        shutil.copy(os.path.join(src_folder, filename), os.path.join(person_folder, filename))

print("Images organized into folders inside 'face_dataset'")
