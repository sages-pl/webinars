result = []
for line in DATA.splitlines():
    line = line.strip()
    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue
    ip, *hosts = line.split()
    row = {'ip': ip, 'hosts': hosts}
    result.append(row)
