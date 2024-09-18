import nnsight
from nnsight import LanguageModel

class NNDIFClient:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        nnsight.CONFIG.set_default_api_key(api_key)
        self.model = LanguageModel(model_name)

    def run_prompt(self, prompt):
        with self.model.trace(prompt, remote=True) as tracer:
            output = self.model.output.save()
            activations = self.model.get_activations()
        return output.value, activations
