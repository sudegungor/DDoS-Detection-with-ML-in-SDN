import os
import sys
from subprocess import Popen, PIPE, STDOUT

script_path = os.path.join('parent.py')
p = Popen(
    [sys.executable, '-u', script_path],
    stdout=PIPE,
    stderr=STDOUT
)
with p.stdout:
    for line in iter(p.stdout.readline, b''):
        print(line),
p.wait()
