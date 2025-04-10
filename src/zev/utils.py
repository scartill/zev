def get_input_string(
    field_name: str,
    prompt: str,
    default: str = "",
    required: bool = False,
) -> str:
    if default:
        prompt = f"{prompt} (default: {default})"
    else:
        prompt = f"{prompt}"

    value = input(prompt + ": ") or default
    if required and not value:
        print(f"{field_name} is required, please try again")
        return get_input_string(field_name, prompt, default, required)
    return value or default
