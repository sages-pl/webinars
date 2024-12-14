header = tuple(DATA[0].keys())
rows = [tuple(row.values()) for row in DATA]

result = []
result.append(header)
result.extend(rows)
