from dotenv import dotenv_values
from pathlib import Path
import questionary

from zev.config.types import (
    SetupQuestion,
    SetupQuestionSelect,
    SetupQuestionText,
    SetupQuestionSelectOption,
)

from zev.llms.ollama.setup import questions as ollama_questions
from zev.llms.openai.setup import questions as openai_questions

setup_questions = [
    SetupQuestionSelect(
        name="LLM_PROVIDER",
        prompt="Pick your LLM provider:",
        options=[
            SetupQuestionSelectOption(
                value="openai",
                label="OpenAI",
                follow_up_questions=openai_questions,
            ),
            SetupQuestionSelectOption(
                value="ollama",
                label="Ollama",
                follow_up_questions=ollama_questions,
            ),
        ],
    )
]


def prompt_question(question: SetupQuestion):
    answers = {}
    if type(question) == SetupQuestionSelect:
        answer: SetupQuestionSelect = questionary.select(
            question.prompt,
            choices=[
                questionary.Choice(option.label, description=option.description, value=option)
                for option in question.options
            ],
        ).ask()
        answers[question.name] = answer.value
        for q in answer.follow_up_questions:
            answers.update(prompt_question(q))
    elif type(question) == SetupQuestionText:
        answer = questionary.text(question.prompt, default=question.default, validate=question.validator).ask()
        answers[question.name] = answer
    else:
        raise Exception("Invalid question type")
    return answers


def run_setup():
    config_path = Path.home() / ".zevrc"
    answers = dotenv_values(config_path) # load in current values and then override as necessary
    for question in setup_questions:
        answers.update(prompt_question(question))
    
    new_file = ""
    for env_var_name, value  in answers.items():
        new_file += f"{env_var_name}={value}\n"

    with open(config_path, "w") as f:
        f.write(new_file)
