import sys
import os
import mmap
from datetime import datetime

def validate_date(date_str):
    """Checks if the date format is valid (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def extract_logs(input_file, input_date, output_dir="output"):
    """Extracts logs for a specific date using memory-mapped files for efficiency."""
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'output_{input_date}.txt')

    target_prefix = input_date.encode('utf-8') + b' '

    try:
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            mmapped_file = mmap.mmap(f_in.fileno(), 0, access=mmap.ACCESS_READ)
            for line in iter(mmapped_file.readline, b""):
                if line.startswith(target_prefix):
                    f_out.write(line)
            mmapped_file.close()
        
        print(f"✅ Logs for {input_date} saved to: {output_file}")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"❌ IO error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    input_date = sys.argv[1]
    if not validate_date(input_date):
        print(f"❌ Invalid date format: {input_date}. Use YYYY-MM-DD.")
        sys.exit(1)

    log_file = 'test_logs.log.txt'
    extract_logs(log_file, input_date)
