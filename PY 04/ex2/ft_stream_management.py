import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_id}: {status}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        stream_management()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        sys.stderr.write("\n[ALERT] Input interrupted by user.")
