## SSH Private Key Generator

This Python script helps you easily generate secure SSH key pairs (ED25519 and optionally RSA) for use in development, cybersecurity, or general system administration. It provides a guided, interactive experience and handles file paths and permissions for you.

### Features
- Generates ED25519 SSH key pairs (recommended)
- Optionally generates RSA key pairs (4096-bit)
- Prompts for key comment, file path, and passphrase
- Handles directory creation and file permissions
- Works on Windows, Linux, and macOS

### Dependencies
- Python 3.x
- `ssh-keygen` must be available in your system's PATH (usually included with OpenSSH)

### Usage
1. Open a terminal in this directory.
2. Run the script:
	```bash
	python ssh-private-keygen.py
	```
3. Follow the prompts:
	- Enter your email (for the key comment)
	- Enter the desired file path for your ED25519 key (or press Enter for default)
	- Enter a passphrase (optional)
	- Choose whether to generate an RSA key as well
	- Enter the desired file path for your RSA key (or press Enter for default)

### Example
```
$ python ssh-private-keygen.py
===Beginning SSH Key Generation===
Enter your email for the key comment (or leave blank): user@example.com
Enter desired ED25519 key file path (default: ~/.ssh/id_ed25519):
Enter a passphrase (leave blank for none):
Create RSA key as well? (y/n): y
Enter desired RSA key file path (default: ~/.ssh/id_rsa):
```

### Notes
- If a key file already exists at the chosen location, `ssh-keygen` will prompt for overwrite.
- On Linux/macOS, private key files are set to `600` permissions for security.
- Passphrases are never displayed or stored by the script.

### License
This project is shared for educational and personal use. Feel free to modify and use as needed.
