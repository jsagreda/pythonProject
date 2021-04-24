# files.py
import sys

f = open(sys.argv[1], mode='rt', encoding='utf-32')
for line in f:
    sys.stdout.write(line)
f.close()
