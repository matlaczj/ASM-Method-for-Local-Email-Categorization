import openai
from experiments import experiments
from prompt_evaluation import run_all_experiments

dataset_path = r"C:\Users\username\Documents\Repozytoria\LM-Based-Email-Categorization-for-User-Defined-Labels\data\dataset_with_possible_categories.csv"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = ""

inference_params = {
    "max_tokens": 1000,
    "seed": -1,
}

run_all_experiments(experiments, dataset_path, inference_params)
