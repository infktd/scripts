
# Import required modules
import subprocess  # For running external commands
import getpass     # For securely getting passphrases
import os          # For file and path operations


def promptUser():
    

    # Prompt for key comment (usually your email)
    print("===Beginning SSH Key Generation===\n")
    keyComment = input("Enter your email for the key comment (or leave blank): ").strip()
    # Get ED25519 key path and passphrase from helper function
    edPath, passPhrase = edPrompt()
    return keyComment, edPath, passPhrase

def generateED29551Key(keyComment, edPath, passPhrase):
    
    # Construct the ssh-keygen command for ED25519
    cmd = ["ssh-keygen", "-t", "ed25519", "-C", keyComment, "-f", edPath]
    
    # Add passphrase to command (empty string if none)
    if passPhrase:
        cmd += ["-N", passPhrase]
    else:
        cmd += ["-N", ""] 
    try:
        print("\n")
        # Run the ssh-keygen command
        subprocess.run(cmd, check=True)
        print("\n✅ ED25519 key generated:\n")
        print(f"  Private key: {edPath}")
        print(f"  Public key: {edPath}.pub")
        # Set permissions on non-Windows systems
        if os.name != 'nt':  # Not Windows
            os.chmod(edPath, 0o600)
        print("\n===Finished SSH Key Generation===\n")
        
    except Exception as e:
        # Print error if key generation fails
        print(f"\n❌ Error generating SSH key: {e}")
        print("\n===Failed SSH Key Generation===\n")    

def generateRSAKey(keyComment, passPhrase, rsaPath):
        
    # Construct the ssh-keygen command for RSA
    cmd = ["ssh-keygen", "-t", "rsa", "-b", "4096", "-C", keyComment, "-f", rsaPath]
    
    # Add passphrase to command (empty string if none)
    if passPhrase:
        cmd += ["-N", passPhrase]
    else:
        cmd += ["-N", ""] 
    try:
        print("\n")
        # Run the ssh-keygen command
        subprocess.run(cmd, check=True)
        print("\n✅ RSA key generated:\n")
        print(f"  Private key: {rsaPath}")
        print(f"  Public key: {rsaPath}.pub")
        # Set permissions on non-Windows systems
        if os.name != 'nt':  # Not Windows
            os.chmod(rsaPath, 0o600)
        print("\n===Finished SSH Key Generation===\n")
        
    except Exception as e:
        # Print error if key generation fails
        print(f"\n❌ Error generating SSH key: {e}\n")
        print("\n===Failed SSH Key Generation===\n")

def edPrompt():

    # Prompt for ED25519 key file path
    edPath = input("Enter desired ED25519 key file path (default: ~/.ssh/id_ed25519): ").strip()
    if not edPath:
        # Use default path if none provided
        edPath = os.path.expanduser("~/.ssh/id_ed25519")
    else:
        edPath = os.path.expanduser(edPath)
    edPath = os.path.normpath(edPath)
    
    # If input is a directory, append default filename
    if os.path.isdir(edPath):
        print("You entered a folder. Appending default filename 'id_ed25519'.")
        edPath = os.path.join(edPath, "id_ed25519")

    # Ensure the directory exists
    dirName = os.path.dirname(edPath)
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok=True)
    # Prompt for passphrase securely
    passPhrase = getpass.getpass("Enter a passphrase (leave blank for none): ").strip()
    return edPath, passPhrase

def rsaPrompt():
    # Prompt for RSA key file path
    rsaPath = input("Enter desired RSA key file path (default: ~/.ssh/id_rsa): ").strip()
    if not rsaPath:
        # Use default path if none provided
        rsaPath = os.path.expanduser("~/.ssh/id_rsa")
    else:
        rsaPath = os.path.expanduser(rsaPath)
    rsaPath = os.path.normpath(rsaPath)
    
    # If input is a directory, append default filename
    if os.path.isdir(rsaPath):
        print("You entered a folder. Appending default filename 'id_rsa'.")
        rsaPath = os.path.join(rsaPath, "id_rsa")

    # Ensure the directory exists
    dirName = os.path.dirname(rsaPath)
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok=True)
    
    return rsaPath

def main():
    
    # Inform user about possible overwrite
    print("\nNote: If any key files exist in chosen location - ssh-keygen will prompt for overwrite.\n")
    
    # Gather user input for ED25519 key
    keyComment, edPath, passPhrase = promptUser()
    # Generate ED25519 key
    generateED29551Key(keyComment, edPath, passPhrase)
    # Optionally generate RSA key
    if input("Create RSA key as well? (y/n): ").strip().lower() =="y":
        rsaPath = rsaPrompt()
        generateRSAKey(keyComment, passPhrase, rsaPath)

main()