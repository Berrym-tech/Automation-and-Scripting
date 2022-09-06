import SyslogCheck
import importlib
importlib.reload(SyslogCheck)

# SSH authentication failures
def su_open(filename, searchTerms):

    # Call syslogCheck and return the results
    is_found = SyslogCheck._syslog(filename,searchTerms)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[5])
    
    # Remove duplication by usinf set
    # and convert the list to a dictionary
    returnedValues = set(found)

    # Print results
    for eachValue in returnedValues:
        print(eachValue)