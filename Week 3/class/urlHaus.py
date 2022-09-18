#
import csv
from importlib.resources import contents
import re
#
def ur1HausOpen(filename,searchTerm):

    with open(filename, newline='') as f:
        contents = csv.reader(f, delimiter=',')
        for skipped_line in range(9):
            next(contents)
            for keyword in searchTerm:
                for eachLine in contents:
                    x = re.findall(r"" + keyword, eachLine[3])
                for skipped_line in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[4]
        print("""
        URL:
        Info: 
        {}""",format(the_url, the_src,"*"+60))