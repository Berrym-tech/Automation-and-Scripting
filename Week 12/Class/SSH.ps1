
# Login to a remote SSH server
#New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential maxwell.berry)


<#

while ($True) {

    # Add a prompt to run commands
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run command on remote SSH server
    (Invoke-SSHCommand -Index 0 $the_cmd).Output

}

#>


Set-SCPItem -Computername '192.168.6.71' -Credential (Get-Credential maxwell.berry)
-Destination '/home/maxwell.berry' -Path '.\Cat.jpg'
