# %%
import openai
import pandas as pd
from utils import (
    strip_punctuation,
    enumerate_and_format_string_list,
    find_closest_match,
    clean_and_split_categories,
)
from typing import Dict, Tuple, List, Optional, Any
import time


def run_all_experiments(
    experiments: List[Dict[str, Any]],
    dataset_path: str,
    inference_params: Dict[str, Any],
) -> None:
    """
    Runs all experiments.

    Args:
        experiments (List[Dict[str, Any]]): The experiments to run.
    """

    for i, experiment in enumerate(experiments):
        start_time = time.time()
        experiment_name = experiment["experiment_name"]
        print(f"Running experiment: {experiment_name}")
        prompt_1 = experiment["prompt_1"]
        prompt_2 = experiment["prompt_2"] if "prompt_2" in experiment else None
        self_consistency = experiment["self_consistency"]
        prompts = [prompt_1, prompt_2] if prompt_2 else [prompt_1]

        evaluate_message_categorizations(
            dataset_path, inference_params, prompts, self_consistency
        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")


def evaluate_message_categorizations(
    dataset_path: str,
    inference_params: Dict[str, Any],
    prompts: List[Dict],
    self_consistency: int,
) -> pd.DataFrame:
    """
    Evaluates message categorizations based on a dataset and inference parameters.

    Args:
        dataset_path (str): The path to the dataset file.
        inference_params (Dict[str, Any]): The parameters for the inference.

    Returns:
        pd.DataFrame: A DataFrame containing the evaluation results.
    """
    records = pd.read_csv(dataset_path).to_dict("records")

    for i, record in enumerate(records):
        actual_category, possible_categories = clean_and_split_categories(
            record["actual_category"], record["possible_categories"]
        )
        message = record["message"]

        response, if_consistent, if_correct = categorize_and_evaluate_message(
            message=message,
            possible_categories=possible_categories,
            actual_category=actual_category,
            inference_params=inference_params,
            prompts=prompts,
            n_tries=self_consistency,
        )
        record.update(
            {
                "response": response,
                "if_consistent": if_consistent,
                "if_correct": if_correct,
            }
        )
        print(
            f"Record {i}: response: {response}, if_consistent: {if_consistent}, if_correct: {if_correct}"
        )

    df = pd.DataFrame(records)
    consistency_ratio = df.if_consistent.sum() / len(df)
    correctness_ratio = df.if_correct.sum() / len(df)
    print(
        f"df.shape: {df.shape} if_consistent: {consistency_ratio} if_correct: {correctness_ratio}"
    )

    return df


def categorize_and_evaluate_message(
    message: str,
    possible_categories: List[str],
    actual_category: str,
    inference_params: Dict,
    prompts: List[Dict],
    n_tries: int = 1,
) -> Tuple[str, bool, bool]:
    """
    Categorizes and evaluates a message based on possible categories and actual category.

    Args:
        message (str): The message to categorize.
        possible_categories List[str]: The possible categories for the message.
        actual_category (str): The actual category of the message.
        inference_params (Dict): The parameters for the inference.
        n_tries (int, optional): The number of tries for the categorization. Defaults to 1.

    Returns:
        Tuple[str, bool, bool]: The most similar answer, and boolean values indicating if the answer is consistent and correct.
    """

    possible_categories_enumerated = enumerate_and_format_string_list(
        possible_categories
    )

    n_prompts = len(prompts)

    answers = []
    for _ in range(n_tries):
        if n_prompts == 2:
            inference_params["max_tokens"] = len(possible_categories) * 50

            completion_1 = generate_chat_completion(
                message=message,
                possible_categories_enumerated=possible_categories_enumerated,
                inference_params=inference_params,
                prompts=prompts,
            )
        else:
            completion_1 = "dummy"

        inference_params["max_tokens"] = 5

        completion_2 = generate_chat_completion(
            message=message,
            possible_categories_enumerated=possible_categories_enumerated,
            inference_params=inference_params,
            previous_completion=completion_1,
            prompts=prompts,
        )

        answer = strip_punctuation(completion_2.choices[0].message["content"]).strip()
        answers.append(answer)

    answer = find_closest_match(
        max(set(answers), key=answers.count), possible_categories
    )
    return answer, answer in possible_categories, answer == actual_category


def generate_chat_completion(
    message: str,
    possible_categories_enumerated: str,
    inference_params: Dict,
    prompts: Dict,
    previous_completion: Optional[openai.ChatCompletion] = None,
) -> openai.ChatCompletion:
    """
    Generates a chat completion using OpenAI's API.

    Args:
        message (str): The message to categorize.
        possible_categories_enumerated (str): The enumerated possible categories.
        inference_params (Dict): The parameters for the inference.
        previous_completion (openai.ChatCompletion, optional): The previous completion, if any. Defaults to None.

    Returns:
        openai.ChatCompletion: The generated chat completion.
    """
    prompt_1 = prompts[0]
    prompt_2 = prompts[1] if len(prompts) == 2 else None

    messages = [
        {
            "role": prompt_1["role"],
            "content": prompt_1["content"].format(
                message,
                possible_categories_enumerated,
            ),
        }
    ]
    if previous_completion:
        if previous_completion != "dummy":
            messages.append(
                {
                    "role": "assistant",
                    "content": previous_completion.choices[0].message["content"],
                }
            )

        try:
            messages.append(
                {
                    "role": prompt_2["role"],
                    "content": prompt_2["content"].format(
                        possible_categories_enumerated,
                    ),
                }
            )
        except:
            if prompt_2:
                messages.append(prompt_2)

    return openai.ChatCompletion.create(
        model="local-model",
        messages=messages,
        **inference_params,
    )
