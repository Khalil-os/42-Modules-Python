def recover_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        data = file.read()
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: File not found.")


if __name__ == "__main__":
    try:
        recover_text("ancient_fragment.txt")
    except Exception as e:
        print(e)
