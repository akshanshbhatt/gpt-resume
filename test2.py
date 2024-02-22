import fitz

doc = fitz.open("sample_resume/charles-stover-resume.pdf")  # open a document
with open("output.txt", "wb") as t_file:  # create a text output
    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf-8")  # get plain text (is in UTF-8)
        t_file.write(text)  # write text of page
        # out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
