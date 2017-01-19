import sys

for line in sys.stdin:
    row = [col.strip() for col in line.split('|')]
    if len(row) == 6 and row[3] and row[4]:
        csv = ','.join(row)
        sys.stdout.write(csv + '\n')
