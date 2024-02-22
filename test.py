from PIL import Image
from prompts import basic_details_text_prompt
from openai import OpenAI
from dotenv import load_dotenv

# Load the enviorment variables
load_dotenv()

# import base64
import os
import io

client = OpenAI(api_key=os.getenv("OAI_API_KEY"))

# Store the content of the text file in a string variable
with open('output2.txt', 'r', encoding="utf-8") as file:
    resume_text = file.read()

# def input_pdf_to_image(uploaded_file_path):

#     first_page = pdf2image.convert_from_path(uploaded_file_path)[0]

#     # Convert to bytes
#     img_byte_arr = io.BytesIO()
#     first_page.save(img_byte_arr, format='JPEG')
#     img_byte_arr = img_byte_arr.getvalue()

#     return base64.b64encode(img_byte_arr).decode('utf-8')  # encode to base64

# op = input_pdf_to_image('sample_resume/charles-stover-resume.pdf')
# print(op)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": basic_details_text_prompt
        },
        {
            "role": "user",
            "content": f'''---RESUME TEXT STARTS---\n{resume_text}\n---RESUME TEXT ENDS---\n\n---JOB TITLE STARTS---\nSoftware Engineering Intern\n---JOB TITLE ENDS---\n\n---JOB DESCRIPTION STARTS---\nThe candidate should be proficient in Python, React framework and have decent knowledge of AWS platform.\n---JOB DESCRIPTION ENDS---
            '''
        }
    ],
    temperature=1,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)
