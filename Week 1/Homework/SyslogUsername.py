import SyslogSchecking
import importlib
importlib.reload(SyslogSchecking)

# SSH authentication failures
def sshd_open(filename, searchTerms):

    # Call syslogCheck and return the results
    is_found = SyslogSchecking._syslog(filename,searchTerms)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[4])
    
    # Remove duplication by usinf set
    # and convert the list to a dictionary
    returnedValues = set(found)

    # Print results
    for eachValue in returnedValues:
        print(eachValue)