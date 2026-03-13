import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: {status}\n")
    print("[ALERT] System diagnostic: Communication channels verified\n",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        stream_management()
    except KeyboardInterrupt:
        print("\n[ALERT] Input interrupted by user.", file=sys.stderr)
    except Exception as e:
        print(e)
