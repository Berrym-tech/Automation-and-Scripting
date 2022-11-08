# Get a list of running processes

# Get a list of members
#Get-Process | Get-Member

# Get a list of processes: namw, id, path
#Get-Process | Select-Object ProcessName, id, Path

# Save the Output to a CSV File
#Get-Process | Select-Object ProcessName, id, Path | Export-Csv -Path C:\Users\maxbe\Desktop\processes.CSV

# System Services
#Get-Service | Get-Member
#Get-Service | Select-Object Status, Name, DisplayName, BinaryPathName |Export-Csv -Path $outputName
#$outputName

$outputName = "C:\Users\maxbe\Desktop\services.csv"

# Get a list of running services
Get-Service | Where-Object { $_.Status -eq "Running" }

# Check to see if the file exists
 if ( Test-Path $outputName ) {

    Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Services File was created!"

}else {

    Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Services File was not created!"

}