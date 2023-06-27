# Artificial Intelligence POCs

Artificial Intelligence - Proof of Concepts

## Pre-Requisites

- [Python 3](https://www.python.org/)
- Open AI module: `pip install openai`
- Cognitive Services module: `pip install azure-cognitiveservices-vision-contentmoderator`

## Running

To be able to run the code, you first need to set the `environment variables` into `run_app.ps1` powershell file. Open this file with a text editor and set the variables there with your API keys and endpoint URLs:

```powershell
$env:OPENAI_API_KEY = "<openai_key>"
$env:OPENAI_URL = "<openai_endpoint_url>"
$env:SUBSCRIPTION_KEY = "<cognitive_services_key>"
$env:SUBSCRIPTION_ENDPOINT = "<cognitive_services_endpoint_url>"
```

After that, you can run this file as a powershell script: `Right Click > Run with PowerShell`.

## Example 1 - Appropriate Article Content

```text
Enter article content: Artificial Intelligence (AI) reshapes companies and how innovation management
is organized. Consistent with rapid technological development and the replacement of human organization,
AI may indeed compel management to rethink a company's entire innovation process. In response, we
review and explore the implications for future innovation management. Using ideas from the Carnegie
School and the behavioral theory of the firm, we review the implications for innovation management
of AI technologies and machine learning-based AI systems. We outline a framework showing the extent
to which AI can replace humans and explain what is important to consider in making the transformation
to the digital organization of innovation. We conclude our study by exploring directions for future research.

"Rethinking Innovation Management: The Implications of AI and Machine Learning"

Artificial Intelligence (AI) reshapes companies and how innovation management is organized.
Consistent with rapid technological development and the replacement of human organization,
AI may indeed compel management to rethink a company's entire innovation process. In response,
we review and explore the implications for future innovation management. Using ideas from the
Carnegie School and the behavioral theory of the firm, we review the implications for innovation
management of AI technologies and machine learning-based AI systems. We outline a framework
showing the extent to which AI can replace humans and explain what is important to consider in
making the transformation to the digital organization of innovation. We conclude our study by
exploring directions for future research.

https://dalleproduse.blob.core.windows.net/private/images/e21e80cd-7c3b-4189-b568-c8955c75e905/generated_00.png?se=2023-06-28T17%3A15%3A34Z&sig=vyaP4fmUw12S5dypk8LUARHhOXfwYpmXX6LtUE7ERBM%3D&ske=2023-07-04T16%3A35%3A56Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-06-27T16%3A35%3A56Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
```

<img src="https://dalleproduse.blob.core.windows.net/private/images/e21e80cd-7c3b-4189-b568-c8955c75e905/generated_00.png?se=2023-06-28T17%3A15%3A34Z&sig=vyaP4fmUw12S5dypk8LUARHhOXfwYpmXX6LtUE7ERBM%3D&ske=2023-07-04T16%3A35%3A56Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-06-27T16%3A35%3A56Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02" width="250px" height="250px"/>

## Example 2 - Inappropriate Article Content (Warning: +18 content)

```
Enter article's content: The Fucking Artificial Intelligence (AI) reshapes companies and
how innovation management is organized. Consistent with rapid technological development
and the replacement of human organization, AI may indeed compel management to rethink a
company's entire innovation process. In response, we review and explore the implications
for future innovation management for this shit. Using ideas from the Carnegie School and
the behavioral theory of the firm, we review the piss off implications for innovation
management of AI technologies and machine learning-based AI systems. We outline a framework
showing the extent to which AI can replace bastard humans and explain what is important to
consider in making the transformation to the digital organization of innovation. We conclude
our study by exploring directions for future research like Motherfuckers.

Content contains inappropriate terms:
- shit
- fucking
- motherfuckers
```
