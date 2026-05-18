import secrets



def generate_token(lenght = 32):
    return secrets.token_hex(lenght)