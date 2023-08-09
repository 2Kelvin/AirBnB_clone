#!/usr/bin/python3
"""Package models' init file"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
