import os
from django.shortcuts import render
from django.http import HttpResponse

# Base directory
BASE_DIR = r"E:\\"


def explore(request, folder_path=""):

    try:

        # Current folder path
        current_path = os.path.join(BASE_DIR, folder_path)

        items = []

        # Read files/folders
        for item_name in os.listdir(current_path):

            # Full path
            item_path = os.path.join(current_path, item_name)

            # Relative path for URL
            relative_path = os.path.relpath(item_path, BASE_DIR)

            # Store details
            items.append({
                "name": item_name,
                "path": relative_path.replace("\\", "/"),
                "is_folder": os.path.isdir(item_path),
                "size": os.path.getsize(item_path),
                "modified_time": os.path.getmtime(item_path),
            })

        context = {
            "items": items,
            "current_path": current_path,
        }

        return render(request, "home.html", context)

    except Exception as e:

        return HttpResponse(f"Error: {e}")