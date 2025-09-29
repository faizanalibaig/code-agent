Streamlit:
  installation:
    - pip install streamlit

  run:
    - python -m streamlit run main.py
  
Dotenv:
  installation:
    - pip install python-dotenv
    
  usage:
    - from dotenv import load_dotenv & import os
    - load_dotenv()  
    - os.getenv("field_name")

OpenAI:        
  installation:
    - pip install openai
    
  usage:
    - from openai import OpenAI
    - create a client by provide a argument api_key to OpenAI()
    - OpenAI(api_key=key)