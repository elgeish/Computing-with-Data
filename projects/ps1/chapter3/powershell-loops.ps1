# Example: a for-loop using a counter
for ($i = 0; $i -lt 5; $i++) { Write-Host $i }

# Example: a while-loop
$i = 0; while ($i -lt 5) { Write-Host $i; $i++ }

# Example: using foreach
foreach ($i in 0..4) { Write-Host $i }

# Example: using .ForEach
(0..4).ForEach({ Write-Host $_ })

# Example: piping to ForEach-Object
(0..4) | ForEach-Object { Write-Host $_ }

# Example: another example of piping to ForEach-Object
Get-Item *.* | Group extension | ForEach-Object { Write-Host $_.Name }
