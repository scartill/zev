from zev.config.types import (
    SetupQuestionSelect,
    SetupQuestionSelectOption,
    SetupQuestionText,
)

questions = (
    SetupQuestionText(
        name="ANTHROPIC_API_KEY",
        prompt="Your Anthropic API key:",
        default="",
    ),
    SetupQuestionSelect(
        name="ANTHROPIC_MODEL",
        prompt="Choose which model you would like to default to:",
        options=[
            SetupQuestionSelectOption(
                value="claude-3-5-sonnet-20240620",
                label="claude-3-5-sonnet-20240620",
                description="Most capable model, best for complex tasks",
            ),
            SetupQuestionSelectOption(
                value="claude-3-5-haiku-20241022",
                label="claude-3-5-haiku-20241022",
                description="Fastest model, good for simple tasks",
            ),
            SetupQuestionSelectOption(
                value="claude-sonnet-4-20250514",
                label="claude-sonnet-4-20250514",
                description="The latest model for complex tasks",
            ),
        ],
    ),
)
