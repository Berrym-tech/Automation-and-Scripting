$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

$var = Read-Host -Prompt "Please enter Windows or IPTables"

# Loop Through the URLs for the rules list
foreach ($u in $drop_urls) {

    # Extract the filename
    $temp = $u.Split("/")
    $file_name = $temp[-1]

    if (Test-Path "./$file_name") {
        continue
    } else {
    # Download the rules list
    Invoke-WebRequest -Uri $u -OutFile "./$file_name"
    }
}

# Array containing the filename
$input_path = @("./compromised-ips.txt","./emerging-botcc.rules")

$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list
Select-String -Path $input_path -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "./ips-bad.tmp"

switch ($var) {
    'Windows' {  
        (Get-Content -Path "./ips-bad.tmp") | % `
        { $_ -replace "^" , "New-NetFirewallRule -DisplayName 'Bad IP Blocker' -Direction OutBound -LocalPort Any -Protocol Any -Action Block -RemoteAddress " -replace "$" } | `
        Out-File -FilePath "./Firewall.ps1"
    }
    'IPTables' {
        (Get-Content -Path "./ips-bad.tmp") | % `
        { $_ -replace "^" , "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
        Out-File -FilePath "./iptables.bash"
        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential maxwell.berry) -Port '2222' `
        -Destination '/home/maxwell.berry/' -Path './iptables.bash'
        New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential maxwell.berry) -Port '2222'
        (Invoke-SSHCommand -index 0 "ls -la").Output
    }
}
