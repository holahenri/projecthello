[app]

# Nom de votre application (remplacez "MyApp" par le nom de votre choix)
title = MyApp

# Nom du package de l'application (généralement sous la forme "com.example.myapp")
package.name = com.example.myapp

# Répertoire où se trouve le code source de votre application
source.dir = .

# Version de votre application
version = 0.1

# Liste des dépendances Python requises par votre application (séparées par des virgules)
requirements = kivy

[buildozer]

# Installez automatiquement les dépendances spécifiées dans requirements
packages = python3, kivy

# Spécifiez les fichiers supplémentaires à inclure dans l'APK (séparés par des virgules)
# Cela peut inclure des images, des polices, etc.
# e.g., include_files = README.md, data/*.png
# include_files =

# Spécifiez les permissions Android nécessaires pour votre application (séparées par des virgules)
# Par exemple, pour autoriser l'accès à Internet, utilisez : INTERNET
# android.permissions = INTERNET

# Ciblez la version de l'API Android
android.api = 27

# Utilisez l'architecture arm64-v8a (d'autres options incluent armeabi-v7a, x86, x86_64, etc.)
android.arch = arm64-v8a

# Spécifiez la version minimale de l'API Android requise
android.minapi = 21

# Utilisez Gradle pour la construction (n'utilisez pas Ant)
android.gradle_dependencies = 'com.android.support:appcompat-v7:28.0.0'

# Spécifiez le chemin vers le répertoire source de Python-for-Android (peut varier selon votre installation)
p4a.source_dir = ~/path/to/python-for-android

