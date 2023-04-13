import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"\n{MESSAGE_COLOR}¡Ya casi terminamos!")
print(f"\nInicializando un repositorio de GIT...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"\n{MESSAGE_COLOR}¡Todo listo!{RESET_ALL}")