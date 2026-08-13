import os
import re
import shutil
import time


# list all files in target diretory
def scan(directory):
    entries = os.scandir(directory)
    files = []

    for entry in entries:
        if entry.is_file():
            files.append(entry.name)

    return files


# sort them by file type and move each of them to their folder
def organize(directory, files):
    counts = {
        "total": 0,
        "moved": 0,
        "skipped": 0,
        "images": 0,
        "videos": 0,
        "documents": 0,
        "apps": 0,
        "audio": 0,
        "compressed": 0,
        "other": 0,
    }

    extensions = {
        "images": ("png", "jpg", "jpeg", "svg", "gif", "bmp", "webp", "tiff", "ico"),
        "videos": ("mp4", "mkv", "avi", "mov", "flv", "wmv", "webm", "m4v"),
        "documents": {
            "txt",
            "pdf",
            "docx",
            "doc",
            "xlsx",
            "xls",
            "pptx",
            "ppt",
            "csv",
            "md",
            "html",
            "json",
            "xml",
            "yaml",
            "yml",
        },
        "apps": (
            "exe",
            "msi",
            "apk",
            "bat",
            "sh",
            "jar",
            "py",
            "rb",
            "pl",
            "php",
            "cpp",
            "c",
            "h",
            "cs",
            "java",
            "js",
            "ts",
            "go",
            "rs",
            "swift",
            "kt",
        ),
        "audio": (
            "mp3",
            "wav",
            "flac",
            "aac",
            "ogg",
            "wma",
            "m4a",
            "alac",
            "opus",
            "aiff",
            "pcm",
        ),
        "compressed": ("zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso", "dmg"),
    }

    # Iterate over files in target directory
    for i, file in enumerate(files):
        extension_match = re.search(r"\.([A-Za-z0-9]+)$", file)
        extension = extension_match.group(1).lower() if extension_match else ""

        for file_type, file_extensions in extensions.items():
            if extension in file_extensions:
                folder = file_type
                break
            else:
                folder = "other"

        source = os.path.join(directory, file)
        destination = os.path.join(directory, folder)

        os.makedirs(destination, exist_ok=True)

        try:
            shutil.move(source, destination)
            counts["moved"] += 1
            counts[file_type] += 1
            print(f"{i + 1}/{len(files)}")
        except shutil.Error:
            print("-file exists in destination already.")
            counts["skipped"] += 1
        except PermissionError:
            print("-Premission denied, Unable to access the file.")
            counts["skipped"] += 1

        counts["total"] += 1
        time.sleep(0.5)

    return {
        "total": counts["total"],
        "moved": counts["moved"],
        "skipped": counts["skipped"],
        "images": counts["images"],
        "videos": counts["videos"],
        "documents": counts["documents"],
        "apps": counts["apps"],
        "audio": counts["audio"],
        "compressed": counts["compressed"],
        "other": counts["other"],
    }
