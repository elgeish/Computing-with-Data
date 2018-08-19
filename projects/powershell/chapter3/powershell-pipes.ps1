# Many aliases are used below for brevity
dir -s * | group extension | Sort-Object count | where count -gt 1 |
select count, name | ConvertTo-Json
