import os
import ctypes
import sys
import random

def run_as_admin():
    try:
        # Check if the script is already running with administrator privileges
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("Running as Admin.")
        else:
            # If not, relaunch the script with administrator privileges
            script = os.path.abspath(sys.argv[0])
            params = " ".join(sys.argv[1:])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, params, 1)
            sys.exit()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

def main():
    try:
        run_as_admin()

        # Print the current working directory
        current_path = os.getcwd()
        print(f"Current Path: {current_path}")

        # Get all filenames in the current working directory
        files = os.listdir(current_path)

        # Rename each file with a random 10-digit number
        for file_name in files:
            if os.path.isfile(file_name):
                new_name = f"{random.randint(1000000000, 9999999999)}{os.path.splitext(file_name)[1]}"
                os.rename(file_name, new_name)
                print(f"Renamed {file_name} to {new_name}")

        # Keep the script open so that the console window remains visible
        input("Press Enter to exit...")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
