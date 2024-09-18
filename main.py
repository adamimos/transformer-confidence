import yaml
from experiment_runner.experiment import Experiment

def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    experiment = Experiment(config)
    experiment.run()

if __name__ == "__main__":
    main()
