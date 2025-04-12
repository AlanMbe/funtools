import os
import shutil

def rename_files(folder, prefix="file_"):
    for index, filename in enumerate(os.listdir(folder)):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}{index}{ext}"
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

def organize_by_type(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            ext = os.path.splitext(filename)[1].lower().strip('.')
            if ext:
                target_dir = os.path.join(folder, ext)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(path, os.path.join(target_dir, filename))
                print(f"Moved: {filename} → /{ext}/")

def delete_empty_folders(folder):
    for root, dirs, _ in os.walk(folder, topdown=False):
        for dir_ in dirs:
            full_path = os.path.join(root, dir_)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                print(f"Deleted empty folder: {full_path}")

def list_files(folder, recursive=False):
    all_files = []
    if recursive:
        for root, _, files in os.walk(folder):
            for file in files:
                all_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path):
                all_files.append(path)
    return all_files

def copy_files(src_folder, dst_folder, ext=None):
    os.makedirs(dst_folder, exist_ok=True)
    for file in os.listdir(src_folder):
        full_path = os.path.join(src_folder, file)
        if os.path.isfile(full_path):
            if ext is None or file.endswith(ext):
                shutil.copy(full_path, os.path.join(dst_folder, file))
                print(f"Copied: {file}")
                
def get_folder_size(folder, human_readable=True):
    total_size = 0
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                total_size += os.path.getsize(path)

    if human_readable:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if total_size < 1024:
                return f"{total_size:.2f} {unit}"
            total_size /= 1024
    else:
        return total_size
