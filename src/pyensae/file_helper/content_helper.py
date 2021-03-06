"""
@file
@brief Various functions to process text
"""

import os

def replace_comma_by_point(file) :
    """
    replaces all commas by point in a file (do that inplace)

    @param      file        file to process
    """
    with open(file,"r") as f : text = f.read()
    text = text.replace(",",".")
    with open(file,"w") as f : f.write(text)

def file_head(filename, nbline = 10, encoding="utf8"):
    """
    extracts the first nbline of a file (assuming it is text file)

    @param      filename        filename
    @param      nbline          number of lines
    @param      encoding        encoding
    @return                     list of lines

    .. versionadded:: 1.1
    """
    if not os.path.exists(filename) :
        raise FileNotFoundError(filename)
    if not os.path.isfile(filename):
        raise FileNotFoundError("{0} is not a file".format(filename))
    rows = [ ]
    with open(filename, "r", encoding=encoding) as f :
        for line in f :
            rows.append(line)
            if len(rows) >= nbline :
                break
    return rows

def file_tail(filename, nbline = 10, encoding="utf8", threshold = 2**14):
    """
    extracts the first nbline of a file (assuming it is text file)

    @param      filename        filename
    @param      nbline          number of lines
    @param      encoding        encoding
    @param      threshold       if the file size is above, it will not read the beginning
    @return                     list of lines

    .. versionadded:: 1.1
    """
    if not os.path.exists(filename) :
        raise FileNotFoundError(filename)
    if not os.path.isfile(filename):
        raise FileNotFoundError("{0} is not a file".format(filename))

    size = os.stat(filename).st_size
    if size < threshold :
        with open(filename, "r", encoding=encoding) as f : rows = f.readlines()
        return rows[-nbline:] if len(rows) > nbline else rows
    else:
        with open(filename, "r", encoding=encoding) as f :
            f.seek(size - threshold)
            content = f.read()
        rows = content.split("\n")
        return rows[-nbline:] if len(rows) > nbline else rows