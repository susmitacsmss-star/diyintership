import os
from django.shortcuts import render
from django.http import HttpResponse

BASE_DIR = r"E:\\"


def explore(request, folder_path=""):

    try:

        current_path = os.path.join(BASE_DIR, folder_path)

        items = []

        for item_name in os.listdir(current_path):

            item_path = os.path.join(current_path, item_name)

            relative_path = os.path.relpath(item_path, BASE_DIR)

            items.append({
                "name": item_name,
                "path": relative_path.replace("\\", "/"),
                "is_folder": os.path.isdir(item_path),
                "size": os.path.getsize(item_path),
                "modified_time": os.path.getmtime(item_path),
            })

        # Breadcrumbs
        breadcrumbs = []

        temp_path = ""

        for part in folder_path.split("/"):

            if part:

                temp_path = os.path.join(temp_path, part)

                breadcrumbs.append({
                    "name": part,
                    "path": temp_path.replace("\\", "/")
                })

        context = {
            "items": items,
            "current_path": current_path,
            "breadcrumbs": breadcrumbs,
        }

        return render(request, "home.html", context)

    except Exception as e:

        return HttpResponse(f"Error: {e}")