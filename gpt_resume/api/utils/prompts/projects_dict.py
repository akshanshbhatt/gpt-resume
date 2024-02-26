import datetime

month_year = datetime.datetime.now().strftime("%m-%Y")

projects_function_prompt = {
    "type": "array",
    "description": "Details of the project done by the candidate.",
    "items": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "Title of the project done by the candidate. If the project is not titled, use 'Untitled Project' as the title.",
            },
            "description": {
                "type": "string",
                "description": "A short description of the project. The project description should not be more than 2 lines. Highlight the main features of the project relevant to the job description.",
            },
            "tech_stack": {
                "type": "array",
                "description": "Tech Stack used in the project.",
                "items": {"type": "string"},
            },
            "time_duration": {
                "type": "object",
                "description": "Start and End date of the project in numerical format (MM-YYYY) only. Do not use words like 'Jan'/'January' in the response.",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start date of the project in MM-YYYY. If there is no start date, return '-' as the start date.",
                    },
                    "end_date": {
                        "type": "string",
                        "description": f"End date of the project in MM-YYYY. If the applicant is still working on the project, use '{month_year}' as the end date. If there are no dates in the project, use '-' as the end date.",
                    },
                    "duration_months": {
                        "type": "integer",
                        "description": "Duration of the project in months. Infer the total duration of the project from the start and end months. If there are no dates associated with the project, return '-' as the duration.",
                    },
                },
            },
            "relevance": {
                "type": "integer",
                "description": "Relevance of the particular project on a scale of 0 to 5 to the job description provided by company. Take the tech stack used, the project description and the duration into account while generating this score. This score should be free from bias of any kind.",
            },
        },
    },
}
