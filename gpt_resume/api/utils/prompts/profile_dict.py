profile_function_prompt = {
    "type": "object",
    "description": "Basic details of the candidate.",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the candidate. If no name is available, use 'Anonymous' as the name. The name is usually present in the beginning of the resume.",
        },
        "email": {"type": "string", "description": "Email of the candidate. If no email is available, use 'no-email@no-email.no' as the email."},
    },
}
