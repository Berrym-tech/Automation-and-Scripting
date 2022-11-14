# Send an Email using Powershell

$toSend = @('maxwell.berry@mymail.champlain.edu','maxberry@optonline.net')

# Message body
$msg = "Hello"

while ($true) {
    
    foreach ($email in $toSend) {

    # Send the email
    Write-Host "Send-MailMessage -from 'maxwell.berry@mymail.champlain.edu' -To $email -Subject "Tisk Tisk" `
    -Body $msg -SmtpServer X.X.X.X"

    # Pause for 1 second
    Start-Sleep 1

    }

}