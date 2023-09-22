from io import TextIOBase
import json
import re

def chunk_read(f_obj: TextIOBase, sentinel: str, max_sentinel: int):
    """Read a file object in chunks
    Read the file object line by line. Each time a sentinel is detected, we increment
    a count. Once the count reaches max_sentinel, we have gatherered the required
    chunk and yield it.
    The function is inspired by this SO answer:
    https://stackoverflow.com/a/42964612/9723036
    NOTE: during chunking, we remove all the white spaces and tabs to reduce the
    memory load.
    :param f_obj: A file object from opening a text file.
    :type f_obj: TextIOBase
    :param sentinel: A string pattern (regex supported) to recognize a specific
        line.
    :type sentinel: str
    :param max_sentinel: Max number of appearance of sentinels allowed in a chunk.
        This is equivalent to a chunk size, but more meaningful than based on only
        line counts.
    :type max_sentinel: int
    :yield: A chunk of the file
    :rtype: Iterator[str]
    """
    cnt, chunk = 0, ''
    for line in f_obj:
        match = re.search(sentinel, line)
        if match:
            cnt += 1
        if cnt <= max_sentinel:
            chunk += line.strip()
        else:
            yield chunk
            cnt = 0
            chunk = line.strip()
    yield chunk

