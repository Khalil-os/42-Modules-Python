def create_archive(filename: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"\nInitializing new storage unit: {filename}")

    try:
        file = open(filename, "w")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        entries = ["[ENTRY 001] New quantum algorithm discovered",
                   "[ENTRY 002] Efficiency increased by 347%",
                   "[ENTRY 003] Archived by Data Archivist trainee"]
        for entry in entries:
            file.write(entry + "\n")
            print(entry)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
        file.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_archive("new_discovery.txt")
