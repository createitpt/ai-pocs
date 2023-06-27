$env:OPENAI_API_KEY = "<openai_key>"
$env:OPENAI_URL = "<openai_endpoint_url>"
$env:SUBSCRIPTION_KEY = "<cognitive_services_key>"
$env:SUBSCRIPTION_ENDPOINT = "<cognitive_services_endpoint_url>"
Invoke-Expression("python main.py")
Read-Host -Prompt "Press ENTER to quit"