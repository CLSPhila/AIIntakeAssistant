import openai
import os
import logging
import re
import json

logger = logging.getLogger(__name__)

def gen_prompt(transcript: str): 
    """

    """
    return(f"""If a person says, 'My name is Mary Smith, and I am 20 years old, and I need help with my disability insurance', the complete data is 

            {{
                "name":"Mary Smith",
                "age": "20",
                "legal problem": "disability insurance"
            }}

            If a person says 'My landlord is evicting me. I'm 45 and my name is George Blink', the complete data is 

            {{
                "name":"George Blink",
                "age": "45",
                "legal problem": "eviction"
            }}

            If a person says, "I'm 33, and just lost my job", the complete data is:

            {{
                "name": "unknown"
                "age":"33",
                "legal problem": "unemployment compensation"
            }}
        
            A person says '{transcript}'. What is the complete data?

            """)


def update_store(store: dict, response):
    """Update the store of the interview with the response from openai

    example response: 
        response["choices"][0]["text"] is ' {\n                "name":"Elliot Green",\n                "age": 68,\n                "legal problem": "unemployment compensation"\n           '

    """
    try:
        patt = re.compile(r".*(?P<data>\{.*\}).*")
        m = patt.match(response["choices"][0]["text"].replace("\n",""))
        if m:
            data = m.group("data").strip()
            structured = json.loads(data)
            data_ = {k:v for k,v in structured.items() if v != "unknown"}
            store.update(data_)
            return store
    except:
        logger.info("Found no json in ")
        logger.info(response)

        




# produces the complete json object.
transcript_demo = "I have been in this city a long time. I am 68 years old, and my name is Elliot Green. I am looking for help because I lost my job." 


incomplete_text = "I want help with my issues, please"
# this works, producing 'unknown' values for all the keys in the json obj.

openai.api_key = os.environ["AIKEY"]

if __name__ == "__main__":

    f = open("../transcribetestmp3.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", f)["text"]
    

    prompt = gen_prompt(transcript)

    #prompt = gen_prompt(transcript_demo)
    #prompt = gen_prompt(incomplete_text)


    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.6,
    max_tokens=50,
    )

    store = update_store(dict(), response)
    print(store)

