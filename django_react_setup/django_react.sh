#!/bin/bash

echo "Creating Folder and cding into it"
mkdir django_react && cd $_

echo "Creating Python virtual env + activation"
python3 -m venv Env
source Env/bin/activate

echo "Installing django via pip and venv"
pip install django djangorestframework

echo "Creating Django Project"
django-admin startproject dj_react .
django-admin startapp leads

