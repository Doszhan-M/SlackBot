import subprocess

with open('parse.sh', 'rb') as file:
    script = file.read()
rc = subprocess.call(script, shell=True)