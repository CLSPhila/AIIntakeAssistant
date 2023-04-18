# AI Intake Assistant

This project demonstrates how modern AI models might be used to assist legal services intakes.

An intake interview can be recorded. An online AI tool can transcribe the interview to text. And then another AI tool (or collection of them) can extract structured data from the transcript. 

This structured data can then be uploaded to a database such as a case or client management system.

This technique is designed to make it easier for intake interviewers and people seeking help to converse naturally and not have their conversation dictated by the needs of a traditional set of structured web forms.


## To try it

- Install with `poetry install`
- Add your OpenAI API key as environment variable called `AIKEY`.
- Create a recording you'd like to use for a test. Simply reading out something like one of the examples in the propmt in app.py will be a good place to start. 
- Run `python app.py`


