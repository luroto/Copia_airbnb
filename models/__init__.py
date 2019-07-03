#!/usr/bin/python3
""" The init file"""
from .engine import file_storage as storing
storage = storing.FileStorage()
storage.reload()
