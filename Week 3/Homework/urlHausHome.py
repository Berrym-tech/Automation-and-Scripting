import csv
import re
def urlHaus(filename, searchTerm):
    with open(filename) as f:
        contents = csv.reader(f)
        for skipped_line in range(9):
            next(contents)
        for eachLine in contents:
            for keyword in searchTerm:
                x = re.findall(keyword, eachLine[2])

                for var in x:
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[6]

# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.

                    print(f"""URL: {the_url}
Info: {the_src}
********************************************
                        """)