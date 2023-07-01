from cryptography.hazmat.primitives import serialization

# Read the PEM file
with open("public.pem", "rb") as pem_file:
    pem_data = pem_file.read()

# Load the RSA key from PEM format
public_key = serialization.load_pem_public_key(pem_data)

# Extract RSA parameters
rsa_parameters = public_key.public_numbers()

# Access the parameters
n = rsa_parameters.n
e = rsa_parameters.e

# Print the parameters
print("Modulus (n):", n)
print("Public exponent (e):", e)
