import csv
import re
# Changed the ur1 (has a 1 instead of an L) to url 
def urlHaus(filename, searchTerm):
# Tabbed out each line individually
    with open(filename) as f:
        contents = csv.reader(f)
# Parsing the CSV's rows
        for skipped_line in range(9):
            next(contents)
# Parsing the CSV's column values
        for eachLine in contents:
            for keyword in searchTerm:
# Find the value of the .tld in this usecase.
                x = re.findall(keyword, eachLine[2])
                if (keyword) in eachLine[2]:
                    e = eachLine[2]
                try: 
                    if keyword in e:
                        for var in x:
 # Makes the URL not clickable by replacing the tt in the URL to xx.
                            the_url = eachLine[2].replace("http","hxxp")
                            the_src = eachLine[7]
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
# Moved the print function to be in the correct loop.
                    print(f"""URL: {the_url}
Info: {the_src}
******************************************* """)
                except:
                    pass