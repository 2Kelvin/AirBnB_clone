#!/usr/bin/python3
"""Package models' init file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
