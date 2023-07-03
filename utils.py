
default_system_prompt = "You are an expert software engineer. You can generate software documentation from fragmented pieces of information."

PROMPT_TEMPLATE_FOR_GENERATION = """{system_prompt}
{user_prompt}
{assistant}
"""


def format_prompt(
    user_prompt: str,
    system_prompt: str = default_system_prompt,
) -> str:

    formatted_prompt = PROMPT_TEMPLATE_FOR_GENERATION.format(
        system_prompt=f"<|im_start|>system\n{system_prompt}<|im_end|>\n",
        user_prompt=f"<|im_start|>user\n{user_prompt}<|im_end|>\n",
        assistant=f"<|im_start|>assistant\n\n",
    )
    return formatted_prompt
