from data_loader.bigbench_loader import BigBenchLoader
from prompt_generator.prompt_builder import PromptBuilder
from nndif_client.nndif_api import NNDIFClient
from utils.logger import Logger
from utils.storage import StorageManager

class Experiment:
    def __init__(self, config):
        self.config = config
        self.logger = Logger(config['log_path'])
        self.storage = StorageManager(config['storage_path'])
        self.loader = BigBenchLoader(config['task_name'])
        self.prompt_builder = PromptBuilder(config['prompt_templates'])
        self.client = NNDIFClient(config['model_name'], config['api_key'])

    def run(self):
        data = self.loader.get_data()
        for idx, item in enumerate(data):
            prompt = self.prompt_builder.build_prompt(
                self.config['prompt_type'], item
            )
            output, activations = self.client.run_prompt(prompt)
            self.storage.save_output(idx, output, activations)
            self.logger.log(f"Processed item {idx}")
