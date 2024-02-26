academic_experience_function_prompt = {
    "type": "object",
    "description": "Details of the college of the candidate. If there are multiple colleges, select the most recent one.",
    "properties": {
        "name": {"type": "string", "description": "Name of the college. If the candidate has not attended any college, use 'No College' as the name of the college."},
        "degree": {
            "type": "string",
            "description": "Degree Received from the college. If the candidate has not received any degree, use 'No Degree' as the degree.",
        },
        "branch": {"type": "string", "description": "Major done during the degree."},
        "start_date": {
            "type": "string",
            "description": "Start date of the degree in MM-YYYY. If the candidate has not started the degree, use '-' as the start date.",
        },
        "end_date": {
            "type": "string",
            "description": "End date of the degree in MM-YYYY. If the candidate is still studying, use 'Present' as the end date.",
        },
    },
}
