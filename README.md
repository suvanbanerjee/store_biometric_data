# Secure Biometric Data Storage [Proof of Concept]

This project demonstrates a Proof of Concept (POC) on how to securely store biometric data on local storage using Python.

## Dataset

The dataset used for this POC is [FVC2000 DB1 B](http://bias.csr.unibo.it/fvc2000/Downloads/DB1_B.zip). This dataset contains fingerprint images that are used to test the biometric storage system.

## Features

- Secure storage of biometric data
- Encryption of biometric data before storage
- Decryption of biometric data for retrieval
- Example code for handling biometric data securely

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

## Usage

1. Prepare the dataset by downloading and extracting it from the provided link.
2. Run the script to store biometric data securely:
  ```bash
  python store_biometric_data.py
  ```
3. Follow the prompts to encrypt and store the biometric data.

## Note

This is a POC and not production-ready code. Do not use this code to actually store biometric data in a real-world application. It is intended for educational purposes only.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [FVC2000](http://bias.csr.unibo.it/fvc2000/) for providing the dataset used in this POC.
