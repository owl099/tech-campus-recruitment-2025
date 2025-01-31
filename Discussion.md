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


to run this 

