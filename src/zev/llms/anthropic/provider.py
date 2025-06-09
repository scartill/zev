from anthropic import Anthropic, AuthenticationError

from zev.config import config
from zev.constants import PROMPT
from zev.llms.inference_provider_base import InferenceProvider
from zev.llms.types import OptionsResponse


class AnthropicProvider(InferenceProvider):
    AUTH_ERROR_MESSAGE = (
        "Error: There was an error with your Anthropic API key. You can change it by running `zev --setup`."
    )

    def __init__(self):
        if not config.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set. Try running `zev --setup`.")

        self.client = Anthropic(api_key=config.anthropic_api_key)
        self.model = config.anthropic_model or "claude-sonnet-4-20250514"

    def get_options(self, prompt: str, context: str) -> OptionsResponse | None:
        try:
            assembled_prompt = PROMPT.format(prompt=prompt, context=context)
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[{"role": "user", "content": assembled_prompt}],
                system="""You must respond with a valid JSON object that matches the OptionsResponse schema. 
The response must be a single JSON object with no additional text or explanation.
The JSON must have this exact structure:
{
    "commands": [
        {
            "command": "string",
            "short_explanation": "string",
            "is_dangerous": boolean,
            "dangerous_explanation": "string or null"
        }
    ],
    "is_valid": boolean,
    "explanation_if_not_valid": "string or null"
}""",
            )

            # Parse the response content as JSON and convert to OptionsResponse
            import json

            try:
                parsed_response = json.loads(response.content[0].text)
                return OptionsResponse(**parsed_response)
            except json.JSONDecodeError:
                print("Error: Claude did not return valid JSON. Please try again.")
                return None

        except AuthenticationError:
            print(self.AUTH_ERROR_MESSAGE)
            return None
