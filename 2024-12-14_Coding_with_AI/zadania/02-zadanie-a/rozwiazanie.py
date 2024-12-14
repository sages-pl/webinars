header = DATA[0]
rows = DATA[1:]
result = [dict(zip(header, row)) for row in rows]
