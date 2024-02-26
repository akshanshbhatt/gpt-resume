from .prompts.profile_dict import profile_function_prompt
from .prompts.projects_dict import projects_function_prompt
from .prompts.relevancy_score_dict import relevancy_score_function_prompt
from .prompts.academic_exp_dict import academic_experience_function_prompt
from .prompts.professional_exp_dict import professional_experience_function_prompt

base_function_prompt = [
    {
        "name": "applicant_details_parser",
        "description": "Parse all the essential details from the text extracted from the resume of the applicant.",
        "parameters": {
            "type": "object",
            "properties": {
                "profile": profile_function_prompt,
                "college": academic_experience_function_prompt,
                "projects": projects_function_prompt,
                "professional_experiences": professional_experience_function_prompt,
                "relevance": relevancy_score_function_prompt,
            },
        },
    }
]
