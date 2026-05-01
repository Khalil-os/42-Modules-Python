import sys
import os
import site


def is_virtual_env():
    return sys.prefix != sys.base_prefix


def print_outside():
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("\nThen run this program again.")


def print_inside():
    env_name = os.path.basename(sys.prefix)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")

    try:
        print(site.getsitepackages()[1])
    except Exception:
        print("Could not retrieve site-packages path.")


def main():
    if is_virtual_env():
        print_inside()
    else:
        print_outside()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
