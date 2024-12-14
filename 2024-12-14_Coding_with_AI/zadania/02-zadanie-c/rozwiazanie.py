result = []
for astronaut in DATA['crew']:
    email = astronaut['email']
    if email.endswith(DOMAINS):
        result.append(email)
