import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"\n{ERROR_COLOR}ERROR: {project_slug=} no es un nombre válido.{RESET_ALL}")

   sys.exit(1)

os.system('cls')
print(f"\n{MESSAGE_COLOR}¡Aquí vamos! ¡Vamos a crear algo increíble!")
print(f"\nCreando proyecto: { os.getcwd() }{RESET_ALL}")