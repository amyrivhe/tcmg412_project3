# testing translating string to datetime

import datetime
line = "[31/Dec/1994:23:59:37 -0700]"

if "[" in line:
    start = line.find("[") + len("[")
    end = line.find("]")
    substring = line[start:end]

    format_str = '%d/%b/%Y:%H:%M:%S %z'
    datetime_obj = datetime.datetime.strptime(substring, format_str)

    print(datetime_obj.year)

