# views.py

import os
from django.shortcuts import render
from django.http import HttpResponse

def file_explorer(request):
    # Base directory you want to explore
    BASE_DIR = r"C:\Users\YourName\Documents"

    try:
        items = []

        # Loop through all files and folders
        for item_name in os.listdir(BASE_DIR):

            # Full path
            item_path = os.path.join(BASE_DIR, item_name)

            # Check if folder
            is_folder = os.path.isdir(item_path)

            # Get size (in bytes)
            size = os.path.getsize(item_path)

            # Get last modified time
            modified_time = os.path.getmtime(item_path)

            # Store details
            items.append({
                "name": item_name,
                "path": item_path,
                "is_folder": is_folder,
                "size": size,
                "modified_time": modified_time,
            })

        context = {
            "items": items,
            "current_path": BASE_DIR
        }

        return render(request, "explorer.html", context)

    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
from django.http import HttpResponse

def home(request):
    return HttpResponse("HELLO BRO YOUR DJANGO IS WORKING 🚀")