
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def test_hash():
    password = "leo1234567"
    print(f"Testing password: {password} (len: {len(password)})")
    try:
        hashed = pwd_context.hash(password)
        print(f"Hashed: {hashed}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_hash()
