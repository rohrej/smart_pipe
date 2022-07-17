# smart_pipe
Wrapper for smart_open to simplify piping data to services and compressing/decompressing

## Quick Start
`pip3 install smart_open[s3]`

`git clone https://rohrej/smart_pipe/`

`cd smart_pipe`

`./pipe.py <input> <output>`

Smart_pipe can also read from stdin and write to stdout, for example:

`cat input.txt | ./pipe.py - s3://your-bucket-name/input.txt.bz2`

Smart_pipe will automatically compress the data based on the filename extension provided.