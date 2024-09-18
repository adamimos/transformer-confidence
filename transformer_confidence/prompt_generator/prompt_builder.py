class PromptBuilder:
    def __init__(self, templates):
        self.templates = templates

    def build_prompt(self, prompt_type, data):
        template = self.templates[prompt_type]
        formatted_choices = "\n".join(
            [f"\t({option['label']}) {option['text']}" for option in data['choices']]
        )
        return template.format(
            question=data['question'],
            choices=formatted_choices,
            answer=data.get('answer', '')
        )
