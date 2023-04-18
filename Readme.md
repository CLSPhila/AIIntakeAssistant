# AI Intake Assistant

This project demonstrates how modern AI models might be used to assist legal services intakes.

An intake interview can be recorded. An online AI tool can transcribe the interview to text. And then another AI tool (or collection of them) can extract structured data from the transcript. 

This structured data can then be uploaded to a database such as a case or client management system.

This technique is designed to make it easier for intake interviewers and people seeking help to converse naturally and not have their conversation dictated by the needs of a traditional set of structured web forms.

The tool takes spoken text, such as 

```
"I have been in this city a long time. I am 68 years old, and my name is Elliot Green. I am looking for help because I lost my job." 
```

And transforms it into a structured dictionary, like

```
{
    "name": "Elliot Green",
    "age": "68",
    "legal problem": "unemployment compensation"
}
```





## To try it

- Install with `poetry install`
- Add your OpenAI API key as environment variable called `AIKEY`.
- Create a recording you'd like to use for a test. Simply reading out something like one of the examples in the propmt in app.py will be a good place to start. 
- Run `python app.py`

## Note: 

Hopefully this is obvious, but in case its not, all names, ages, etc. in this repository are totally made up. Any correspondence with any real people, living or dead, would be totally coincidental.
