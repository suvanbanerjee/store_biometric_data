from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
import io

class Settings(BaseSettings):
  app_name: str = "Encryption and Decryption using ChaCha20"
  debug: bool = False
  admin_email: str = "banerjeesuvan@gmail.com"

settings = Settings()
app = FastAPI()

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD")
SALT = os.urandom(16)

def derive_key(password: str, salt: bytes) -> bytes:
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
  )
  return kdf.derive(password.encode())

def encrypt_image(image_data: bytes, key: bytes) -> bytes:
  nonce = os.urandom(16)
  cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
  encryptor = cipher.encryptor()
  encrypted_data = nonce + encryptor.update(image_data) + encryptor.finalize()
  return encrypted_data

def decrypt_image(encrypted_data: bytes, key: bytes) -> bytes:
  nonce = encrypted_data[:16]
  cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
  decryptor = cipher.decryptor()
  decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
  return decrypted_data

@app.get("/")
async def read_root():
    return {"message": "Send a POST request to /encrypt/ or /decrypt/ endpoint with an file to encrypt or decrypt it."}

@app.post("/encrypt/")
async def encrypt_image_endpoint(file: UploadFile = File(...)):
  image_data = await file.read()
  password = MASTER_PASSWORD
  if not password:
    raise HTTPException(status_code=500, detail="Encryption password not set in environment variables.")
  key = derive_key(password, SALT)
  encrypted_data = encrypt_image(image_data, key)
  encrypted_file = io.BytesIO(encrypted_data)
  return StreamingResponse(encrypted_file, media_type="application/octet-stream", headers={
    "Content-Disposition": f"attachment; filename={file.filename}.enc"
  })

@app.post("/decrypt/")
async def decrypt_image_endpoint(file: UploadFile = File(...)):
  encrypted_data = await file.read()
  password = MASTER_PASSWORD
  if not password:
    raise HTTPException(status_code=500, detail="Encryption password not set in environment variables.")
  key = derive_key(password, SALT)
  try:
    decrypted_data = decrypt_image(encrypted_data, key)
  except Exception:
    raise HTTPException(status_code=400, detail="Decryption failed. Check the password or the file.")
  decrypted_file = io.BytesIO(decrypted_data)
  return StreamingResponse(decrypted_file, media_type="application/octet-stream", headers={
    "Content-Disposition": f"attachment; filename={file.filename.replace('.enc', '')}"
  })

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
