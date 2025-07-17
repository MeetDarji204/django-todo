@echo off 
:: This is a Windows-compatible build script 
python -m pip install -r requirements.txt 
python manage.py collectstatic --noinput 
python manage.py migrate 
