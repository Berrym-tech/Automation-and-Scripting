import logcheck
import importlib
importlib.reload(logcheck)

# Apache Events
def apache_events(filename, service, term):

    # Call syslogCheck and return the results
    is_found = logcheck._logs(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        # GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
        found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])
    
    # Remove duplication by usinf set
    # and convert the list to a dictionary
    getValues = set(found)

    # Print results
    for eachValue in getValues:

        print(eachValue)