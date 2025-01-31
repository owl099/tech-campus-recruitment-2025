import sys
import os

def extract_logs(log_file, date):
    """Extract logs for a given date and save them to an output file."""
    
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    try:
        with open(log_file, "r") as file, open(output_file, "w") as output:
            for line in file:
                if line.startswith(date):
                    output.write(line)
        
        print(f"✅ Logs for {date} saved in: {output_file}")
    
    except FileNotFoundError:
        print("❌ Error: Log file not found. Please check the file path.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    log_file = "test_logs.log.txt"  # Ensure this file is downloaded beforehand
    
    extract_logs(log_file, date)
