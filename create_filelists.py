#CREATED BY GEMINI-------------------------------

import os

# 1. Define your paths clearly
# The folder where your processed videos actually live
preprocessed_root = "filelists/subset_data_preprocessed"
# The folder where you want to save train.txt
output_dir = "filelists" 

video_folders = []

# 2. Scan the directory
for root, dirs, files in os.walk(preprocessed_root):
    if "audio.wav" in files:
        # Get the full path to the video folder
        # e.g. "filelists/subset_data_preprocessed/video1"
        full_path = root
        
        # We only want the folder name relative to the preprocessed root
        # This removes "filelists/subset_data_preprocessed/" from the string
        clean_name = os.path.relpath(full_path, preprocessed_root)
        
        # Fix Windows backslashes to forward slashes
        clean_name = clean_name.replace("\\", "/")
        
        video_folders.append(clean_name)

print(f"Found {len(video_folders)} video folders.")
print(f"Example entry: {video_folders[0] if video_folders else 'None'}")

# 3. Write the files
if video_folders:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/train.txt", "w") as f:
        f.write('\n'.join(video_folders))
    
    with open(f"{output_dir}/val.txt", "w") as f:
        f.write('\n'.join(video_folders))

    print(f"Success! Created {output_dir}/train.txt and {output_dir}/val.txt")
else:
    print("No videos found. Check your preprocessed_root path.")