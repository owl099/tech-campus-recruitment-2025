To efficiently extract logs for a given date from a 1 TB log file, we can consider multiple approaches, each with its own pros and cons depending on the system's resources and storage type.

 1. Line-by-Line Streaming (Simple Approach)
Method:

Read the file line by line.
Check if the line starts with the target date.
Write matching lines to an output file.

 2. Buffered Reading (Chunk-Based Processing)
Method:

Instead of reading one line at a time, read chunks of data (e.g., 1 MB at a time).
Process the chunk in memory and write matches to the output.

3. Memory-Mapped Files (mmap)
Method:

Use memory-mapped files (mmap) to treat the file as an array of bytes.
Scan for the target date without loading everything into RAM.

For processing a 1 TB log file with sequential reads and date-based filtering, the buffered binary read approach is used because:
Optimized for Sequential Access
No Virtual Memory Overhead
Portability and Reliability
Simpler Error Handling


to run this :
1. Prerequisites
  Install Python (python3 --version).
2.download the log file :
  To download the log file, run the following command in your terminal:

  curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"
3. save it wit the name as test_logs.log.txt and place in teh same directory.
4.use the command
Usage: python extract_logs.py YYYY-MM-DD   



