## 0x03-log_parsing

### Description

This project is about parsing logs. It is a simple script that reads stdin line by line and computes metrics.
Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (If the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  - Total file size: File size: `<total size>`
  - where `<total size>` is the sum of all previous `<file size>` (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code does not appear, don’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

### Usage
    
    ```bash
    $ ./0-stats.py


### Example
    
    ```bash
    $ cat some_file.log | ./0-stats.py
    File size: 9
    200: 2
    401: 1
    403: 1
    404: 1
    405: 1
    File size: 19
    200: 4
    401: 2
    403: 2
    404: 2
    405: 2
    File size: 29
    200: 6  
    401: 3
    403: 3
    404: 3
    405: 3
    ^C
    File size: 39

### Author
Hillary Oyaro
