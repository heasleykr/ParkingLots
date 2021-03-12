#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

'''
This is a web application built for San Diego Global Knowledge Univeristy

Author: Katelynn Heasley
Date: 03/11/2021

This application is a rental website for private parking spaces. Users can list their own parking spaces or rent from others. 
Designed for a culminating final project for the Full Stack Immersive Coding Program. 

'''

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
