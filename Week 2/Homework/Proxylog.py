import Proxycheck
import importlib
importlib.reload(Proxycheck)

# Apache Events
def QQexe_events(filename, service, term):

    # Call syslogCheck and return the results
    is_found = Proxycheck._logs(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        #print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        # GET /cgi-bin/test-cgi HTTP/1.1" 404 435 "-" "-"
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + "bytes sent," + sp_results[7] + "bytes recieved.")

    # Remove duplication by usinf set
    # and convert the list to a dictionary
    getValues = (found)


    # Print results
    for eachValue in getValues:

        print(eachValue)

def QQ_open_events(filename, service, term):

    is_found = Proxycheck._logs(filename, service, term)

    found = []


    for eachFound in is_found:
        if ("open" in eachFound):
            found.append(eachFound)

    getValues = (found)

    for eachValue in getValues:

        print(eachValue)


