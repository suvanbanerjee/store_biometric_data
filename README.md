# Secure Biometric Data Storage [Proof of Concept]

This project demonstrates a Proof of Concept (POC) on how to securely store biometric data on local storage using ChaCha20-Poly1305 encryption. 

## Dataset

The dataset used for this POC is [FVC2000 DB1 B](http://bias.csr.unibo.it/fvc2000/Downloads/DB1_B.zip). This dataset contains fingerprint images that are used to test the biometric storage system. 

## Requirements

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. Clone the repository:
  ```bash
  git clone /home/suvanbanerjee/Desktop/store_biometric_data
  ```
2. Navigate to the project directory:
  ```bash
  cd store_biometric_data
  ```
3. Install the required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```
4. Chage the directory to the `app` folder:
  ```bash
  cd app
  ```
5. Run FastAPI server:
  ```bash
  fastapi dev main.py
  ```

note: make to to create the .env file in app directory

## Usage

Method 1: Using the FastAPI Docs
1. Open the FastAPI docs in your browser: `http://127.0.0.1:8000/docs`
2. Click on the `POST /encrypt` endpoint.
3. Click on the `Try it out` button.
4. Upload a fingerprint image file.
5. Click on the `Execute` button.
6. In response, you will get the encrypted data and download the same.

Method 2: Sending a POST request to the `/encrypt` or `/decrypt` endpoint
1. Use a tool like `curl` or `Postman` to send a POST request to the `/encrypt` or `/decrypt` endpoint.


## Note

This is a POC and not production-ready code. Do not use this code to actually store biometric data in a real-world application. It is intended for educational purposes only.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [FVC2000](http://bias.csr.unibo.it/fvc2000/) for providing the dataset used in this POC.