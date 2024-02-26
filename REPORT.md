# Report
## Deliverables Checklist
These were the deliverables asked according to the assignment description along with the status of completion from my end -

 - [x] Create a web interface where a user can (1) feed N resumes and (2) add some inputs.
 - [x] This interface must generate a specific output in JSON format (mentioned in the Requirements section). Showcase this output data on the web.
 - [x] You have to submit a link to your Github repository for this assignment submission.
-  [x] The Github repository should contain following essential things -
    - [x]  Python (Django) code files (.py) containing your implementation.
    - [x]  `requirements.txt` file consisting of all the python dependencies used in your submission
    - [x]  A `README` file with instructions to run the code in order to generate the JSON output as mentioned
    - [x]  A short report documenting your approach, including details of the implementation, hyperparameters, evaluation results, and any insights gained.
- [x]  Design a web interface (React) to showcase the working of this project as per the Figma design. Adhere to the Figma designs provided. [**I've tried my best. I have relatively less experience with frontend development.**]

### Design Comparisons
Here is a side-by-side comparison of what was asked and what I delivered. It's not perfect by any means, but this is the best I could get.
|Figma Design|My Implementation|
|--|--|
|![Upload Screen](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/bd04b151-7538-40b8-b9f8-b617f33fe348)|![Screenshot_26-2-2024_115757_localhost](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/598762d7-c4a4-4e5a-a630-ed3d23bbba5a)|
|![Uploading](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/efc48014-c8d9-4027-a404-f33a248e1031)|![Screenshot_26-2-2024_115821_localhost](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/f97b4ee2-e6f7-455a-b54c-fca80e3acee6)|
|![Modal](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/26cbdd30-3183-45d5-bf68-9223d7150cd5)|![Screenshot_26-2-2024_115919_localhost](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/45691591-3653-4ba6-816b-72ed93eb221e)|
|![Filtered](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/2321ac0c-dd81-4587-9101-babde8d51761)|![Screenshot_26-2-2024_12011_localhost](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/70bf9a86-31c4-4580-9e5e-52e9ecefdfa8)|
|![Profile View](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/258d6bad-f52e-402e-8d84-7d0d3c2292f7)|![Screenshot_26-2-2024_12151_localhost](https://github.com/akshanshbhatt/gpt-resume/assets/53227127/0a07c5db-8a60-430e-9ab0-2ae670654c40)|

## Project Decisions and Rationale
### **Using PyMuPDF for PDF Text Extraction**
PyMuPDF is the fastest Python library when it comes to data extraction from PDF files. It is a Python wrapper for the MuPDF library, which is written in C (main reason why it's so fast). It was a no-brainer for me to use it instead of any other Python library. You can read more about [performance comparison](https://pymupdf.readthedocs.io/en/latest/about.html#performance) and [methodologies used](https://pymupdf.readthedocs.io/en/latest/app4.html).
### **Using Multithreading for Parallelization**
I deployed multiple threads to extract text from the PDFs and dispatch the requests to the OpenAI api. This significantly brought down the latency of the backend. All the computation is parallelized. To bring into perspective, when I submitted 10 PDF files without multithreading, it took about 40 seconds to get the final response from the server and with multithreading it only took ~7-8 seconds, which is a huge improvement.

### **Using Nextjs for Frontend**
Nextjs offers several advantages over regular React. It simplifies React application development by providing built-in server-side rendering (SSR), automatic code splitting, and a straightforward file-based routing system. Nextjs simplifies the development process by handling many configuration details out of the box, allowing developers to focus more on building features and less on setup and optimization tasks. UI component libraries such as `shadcn/ui` also work out-of-the-box with Nextjs since both are maintained by Vercel. 

### **Using Axios as the HTTP Client**
  
Axios is a popular choice for handling HTTP requests in Next.js apps due to its simplicity, flexibility, and widespread adoption in the JavaScript ecosystem. It provides a clean and concise API for making requests, supports promises, and has built-in features for interceptors, request/response transformations, and automatic JSON parsing.

### **Using Page-based Routing**
Apparantly, `Pages`-based routing is the [preferred routing strategy](https://stackoverflow.com/a/76660152) when making client-side application.
### **Using `functions` Parameter**
When making API calls to OpenAI, I used the `functions` parameter in the request, which gave a more refined output for direct use.
Source: [How to call functions with chat models | OpenAI Cookbook](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)
### **PDF Pages Text Extraction Limit**
To avoid mistakenly uploading large PDF files and exhausting all your token credits in the process, I implemented a page limit up to which the text will be extracted. The text will only be extracted up to page 3 of the PDF file to avoid any catastrophic damage.

## Future Scope
This is just a basic prototype of the product in the making. Here are a few things that can be improved/added -
* **Refining the frontend**
* **Making the prompts more robust**
* **Adding support for GPT-4 Image prompt support to skip the text extraction process altogether**
* **Handling edge cases in resumes**
* **Adding additional security features**
