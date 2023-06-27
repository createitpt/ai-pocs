$env:OPENAI_API_KEY = "<openai_key>"
$env:SUBSCRIPTION_KEY = "<cognitive_services_key>"
Invoke-Expression("python main.py")
Read-Host -Prompt "Press ENTER to quit"