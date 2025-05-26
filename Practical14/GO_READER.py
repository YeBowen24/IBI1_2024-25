import os
import subprocess

def main():
    script_name_DOM = "go_reader(DOM).py"
    script_name_SAX = "go_reader(SAX).py"
    try:
        subprocess.call(["python", script_name_DOM])
    except Exception as e:
        print(f"Error occurred while running {script_name_DOM}: {e}")
    try:
        subprocess.call(["python", script_name_SAX])
    except Exception as e:
        print(f"Error occurred while running {script_name_SAX}: {e}")
    print()
    print('SAX is faster')

if __name__ == "__main__":
    main()