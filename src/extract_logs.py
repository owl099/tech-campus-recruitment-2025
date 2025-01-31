import sys
import os
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def extract_logs(log_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    target_prefix = date.encode('utf-8') + b' '  # Fix: Include trailing space
    
    try:
        # Binary mode + buffering for performance
        with open(log_file, "rb", buffering=1024*1024) as file, \
             open(output_file, "wb") as output:
            for line in file:
                if line.startswith(target_prefix):
                    output.write(line)
        
        print(f"✅ Logs for {date} saved in: {output_file}")
    
    except FileNotFoundError:
        print("❌ Error: Log file not found. Please check the file path.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    if not validate_date(date):
        print(f"❌ Invalid date format: {date}. Use YYYY-MM-DD.")
        sys.exit(1)
    
    log_file = "test_logs.log.txt"  # Fixed filename (no .txt)
    extract_logs(log_file, date)
