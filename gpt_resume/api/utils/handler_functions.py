import datetime

month_year = datetime.datetime.now().strftime("%m-%Y")

PROJECTS_FUNCTION = {
    "type": "array",
    "description": "Details of the projects done by the candidate",
    "items": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "Title of the project done by the candidate. If the project is not titled, use 'Untitled Project' as the title."
            },
            "description": {
                "type": "string",
                "description": "A short description of the project. The project description should not be more than 2 lines. Highlight the main features of the project relevant to the job description."
            },
            "tech_stack": {
                "type": "array",
                "description": "Tech Stack used in the project",
                "items": {
                    "type": "string"
                }
            },
            "time_duration": {
                "type": "object",
                "description": "Start and End date of the project",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start date of the project in MM-YYYY"
                    },
                    "end_date": {
                        "type": "string",
                        "description": f"End date of the project in MM-YYYY. If the applicant is still working on the project, use '{month_year}' as the end date."
                    },
                    "duration_months": {
                        "type": "integer",
                        "description": "Duration of the project in months"
                    }
                }
            },
            "relevance": {
                "type": "integer",
                "description": "Relevance of the project in a scale of 0 to 5 to the job description provided by company"
            }
        }
    }
}

PROFESSIONAL_EXPERIENCE_FUNCTION = {
    "type": "array",
    "description": "Details of the professional experiences of the candidate",
    "items": {
        "type": "object",
        "properties": {
            "organization": {
                "type": "string",
                "description": "Name of the organization."
            },
            "role": {
                "type": "string",
                "description": "Role in the organization."
            },
            "tech_stack": {
                "type": "array",
                "description": "Tech Stack used in the project.",
                "items": {
                    "type": "string"
                }
            },
            "description": {
                "type": "string",
                "description": "Description of the project."
            },
            "time_duration": {
                "type": "object",
                "description": "Start and End date of the project.",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start date of the project in MM-YYYY."
                    },
                    "end_date": {
                        "type": "string",
                        "description": f"End date of the project in MM-YYYY. If the applicant is still working there, use '{month_year}' as the end date."
                    },
                    "duration_months": {
                        "type": "integer",
                        "description": "Duration of the project in months."
                    }
                }
            },
            "relevance": {
                "type": "integer",
                "description": "Relevance of the professional experience in a scale of 0 to 5 to the job description provided by company."
            }
        }
    }
}

COLLEGE_FUNCTION = {
    "type": "object",
    "description": "Details of the college of the candidate. If there are multiple colleges, select the most recent one. If the candidate has not attended any college, use 'No College' as the name of the college.",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the college."
        },
        "degree": {
            "type": "string",
            "description": "Degree Received from the college."
        },
        "branch":{
            "type": "string",
            "description": "Major done during the degree."
        },
        "start_date":{
            "type": "string",
            "description": "Start date of the degree in MM-YYYY."
        },
        "end_date":{
            "type": "string",
            "description": f"End date of the degree in MM-YYYY. If the candidate is still studying, use '{month_year}' as the end date."
        }
    }
}

PROFILE_FUNCTION = {
    "type": "object",
    "description": "Details of the candidate.",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the candidate. If no name is available, use 'Anonymous' as the name."
        },
        "email": {
            "type": "string",
            "description": "Email of the candidate."
        }
    }

}

RELEVANCE = {
    "type": "integer",
    "description": "Relevance of the  to the job description in a scale of 0 to 100. If the text inputted is empty or irrelevant, use 0 as the relevance score. If the text inputted is highly relevant, use 100 as the relevance score. If the relevance score is between 0 and 100, use the relevance score as the relevance score."
}

JSON_FUNCTION = [
    {
        "name": "parse_resume",
        "description": "Parse the resume and return the details of the candidate.",
        "parameters": {
            "type": "object",
            "properties": {
                "profile": PROFILE_FUNCTION,
                "college": COLLEGE_FUNCTION,
                "projects": PROJECTS_FUNCTION,
                "professional_experiences": PROFESSIONAL_EXPERIENCE_FUNCTION,
                "relevance": RELEVANCE,
            }
        },
    }
]
