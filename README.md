# Artificial Intelligence POCs

Artificial Intelligence - Proof of Concepts

## Pre-Requisites

- [Python 3](https://www.python.org/)
- Open AI module: `pip install openai`
- Cognitive Services module: `pip install azure-cognitiveservices-vision-contentmoderator`

## Running

To be able to run the code, you first need to set the `environment variables` into `run_app.ps1` powershell file. Open this file with a text editor and set the variables there with your API keys. After that, you can run this file `Right Click > Run with PowerShell`.

## Example 1 - Appropriate Article Title

```text
Enter article title: How to innovate using AI services
Title: How to innovate using AI services
Image: https://dalleproduse.blob.core.windows.net/private/images/7617047b-9dc0-4464-98be-806acebbc21d/generated_00.png?se=2023-06-28T12%3A16%3A26Z&sig=al0bgdUPyiy2orU4cYk1Xej6XkV6a22h6V9C%2BPmXMQM%3D&ske=2023-07-04T11%3A41%3A43Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-06-27T11%3A41%3A43Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02
```

<img src="https://dalleproduse.blob.core.windows.net/private/images/7617047b-9dc0-4464-98be-806acebbc21d/generated_00.png?se=2023-06-28T12%3A16%3A26Z&sig=al0bgdUPyiy2orU4cYk1Xej6XkV6a22h6V9C%2BPmXMQM%3D&ske=2023-07-04T11%3A41%3A43Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2023-06-27T11%3A41%3A43Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02" width="250px" height="250px"/>

## Example 2 - Inappropriate Article Title

```
Enter article title: How to innovate using fucking AI services
Content contains inappropriate terms: ['fucking']
```
