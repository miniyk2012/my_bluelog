
from werkzeug.security import generate_password_hash, check_password_hash

if __name__ == '__main__':
    print(generate_password_hash('123'))