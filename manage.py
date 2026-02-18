#!/usr/bin/env python
import json
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    file_path = "cinema_db_data.json"
    if len(sys.argv) > 2:
        if sys.argv[2] == "loaddata":
            file_path = sys.argv[3]

    with open(file_path, "r") as file:
        data = json.load(file)
