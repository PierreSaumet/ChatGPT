import json
import os
import sys

import openai

from dotenv import load_dotenv

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# General messages    
error_use_msg = "Error, please enter: " + color.BOLD + "python main.py --help" + color.END
error_conf_open_msg = color.RED + "Error with the settings file, cannot open it..." + color.END
error_cong_read_msg = color.RED + "Error with the settings file. cannot read it." + color.END

help_msg = color.RED + "How to use this program?\n\n" + color.END \
    + "1) To display help:\n" \
    + color.BOLD + "\tpython main.py --help\n\n" + color.END \
    + "2) To make a 'ChatGPT' request:\n" \
    + color.BOLD + '\tpython main.py "AND YOUR TEXT"' + color.END\
    + "\nfor example:\n" \
    + color.GREEN + '\t python main.py "Hello, you are a marketing consultant. I want to create a nice add on Tiktok. Give me some advice"\n\n' + color.END


def get_settings() -> dict:
    # Open JSON file
    try:
        f = open('openai_conf.json')
    except OSError:
        print(error_conf_open_msg)
        sys.exit(1)

    # Read file
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        print(error_cong_read_msg)
        sys.exit(1)

    return data

def call_api(msg: str, data: dict) -> str:

    try:
        response_openai = openai.Completion.create(
            engine=data['model'],
            prompt=msg,
            temperature=data['temperature'],
            max_tokens=data["max_tokens"],
            top_p=data["top_p"],
            stream=data["stream"],
        )
    except openai.error.Timeout as e:
        #Handle timeout error, e.g. retry or log
        print(f"OpenAI API request timed out: {e}")
        sys.exit(1)
    except openai.error.APIError as e:
        #Handle API error, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        sys.exit(1)
    except openai.error.APIConnectionError as e:
        #Handle connection error, e.g. check network or log
        print(f"OpenAI API request failed to connect: {e}")
        sys.exit(1)
    except openai.error.InvalidRequestError as e:
        #Handle invalid request error, e.g. validate parameters or log
        print(f"OpenAI API request was invalid: {e}")
        sys.exit(1)
    except openai.error.AuthenticationError as e:
        #Handle authentication error, e.g. check credentials or log
        print(f"OpenAI API request was not authorized: {e}")
        sys.exit(1)
    except openai.error.PermissionError as e:
        #Handle permission error, e.g. check scope or log
        print(f"OpenAI API request was not permitted: {e}")
        sys.exit(1)
    except openai.error.RateLimitError as e:
        #Handle rate limit error, e.g. wait or log
        print(f"OpenAI API request exceeded rate limit: {e}")
        sys.exit(1)

    if response_openai["choices"][0]["text"][:2] == "\n\n":
        return response_openai["choices"][0]["text"][2:]
    return response_openai["choices"][0]["text"]

def do_request(msg: str) -> None:
    # Load your OPENAI token
    load_dotenv()
    TOKEN = os.getenv('TOKEN_OPENAI')

    # Connect to the openai api
    openai.api_key = TOKEN

    # Get settings
    data = get_settings()

    print(color.BOLD + "\t\t waiting... " + color.END)
    
    # Call OpenAI API
    rep = call_api(msg, data)

    # Put colors
    you_msg = color.GREEN + "ME:\t\t" + color.END + msg + "\n"
    openai_msg = color.BLUE + "CHATGPT:\t" + color.END + rep

    # Display msg
    print(you_msg)
    print(openai_msg)   


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            print(help_msg)
            sys.exit(0)
        else:
            do_request(sys.argv[1])
            sys.exit(0)
    else:
        print(error_use_msg)
        sys.exit(1)
