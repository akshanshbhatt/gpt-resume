import datetime

month_year = datetime.datetime.now().strftime("%m-%Y")

professional_experience_function_prompt = {
    "type": "array",
    "description": "Details of the professional experience of the applicant.",
    "items": {
        "type": "object",
        "properties": {
            "organization": {
                "type": "string",
                "description": "Name of the organization. If the applicant has not worked anywhere, use '-' as the name of the organization.",
            },
            "role": {"type": "string", "description": "Role in the organization. If the applicant has not worked anywhere, use '-' as the role."},
            "tech_stack": {
                "type": "array",
                "description": "Tech Stack used during the work.",
                "items": {"type": "string"},
            },
            "description": {
                "type": "string",
                "description": "A short description of the work done during his time in the organization. The description should not be more than 2 lines. Highlight the main features of the professional experience relevant to the job description. If the applicant has not worked anywhere, use '-' as the description.",
            },
            "time_duration": {
                "type": "object",
                "description": "Start and End date of the professional experience in numerical format (MM-YYYY) only. Do not use words like 'Jan'/'January' in the response.",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start date of the professional experience in MM-YYYY.",
                    },
                    "end_date": {
                        "type": "string",
                        "description": f"End date of the professional experience in MM-YYYY. If the applicant is still working there, use '{month_year}' as the end date.",
                    },
                    "duration_months": {
                        "type": "integer",
                        "description": "Duration of the professional experience in months.",
                    },
                },
            },
            "relevance": {
                "type": "integer",
                "description": "Relevance score of the professional experience in a scale of 0 to 10 to the job description provided by company. Take the tech stack used, the work description and the duration into account while generating this score. This score should be free from bias of any kind. If the professional experience is not relevant, use 0 as the relevance score.",
            },
        },
    },
}
