def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        with open("classified_vault.txt", "r") as file:
            data = file.read()
            print(data)

        print("\nSECURE PRESERVATION:")
        with open("security_archive.txt", "w") as file:
            entry = "[CLASSIFIED] New security protocols archived\n"
            file.write(entry)
            print(entry)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")

    except FileNotFoundError:
        print("ERROR: File not found.")


if __name__ == "__main__":
    try:
        vault_security()
    except Exception as e:
        print(e)
