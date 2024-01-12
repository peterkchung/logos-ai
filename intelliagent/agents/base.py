import os
from huggingface_hub import InferenceClient

"""
https://huggingface.co/docs/huggingface_hub/v0.20.2/en/package_reference/inference_client#huggingface_hub.InferenceClient

:params:
:model (str, optional) — The model to run inference with. Can be a model id hosted on the Hugging Face Hub, e.g. bigcode/starcoder or a URL to a deployed Inference Endpoint. Defaults to None, in which case a recommended model is automatically selected for the task.

:token (str, optional) — Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

:timeout (float, optional) — The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

:headers (Dict[str, str], optional) — Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.
:cookies (Dict[str, str], optional) — Additional cookies to send to the server.

"""

default_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

client = InferenceClient(
    model = default_model,
    token = False
)


"""
research agent
text-classification > action

https://huggingface.co/docs/huggingface_hub/v0.20.2/en/package_reference/inference_client#huggingface_hub.InferenceClient.text_classification

:params:
:text (str) — A string to be classified.

:model (str, optional) — The model to use for the text classification task. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed Inference Endpoint. If not provided, the default recommended text classification model will be used. Defaults to None.

"""

client.text_classification(
    
)



"""
https://huggingface.co/docs/huggingface_hub/v0.20.2/en/package_reference/inference_client#huggingface_hub.InferenceClient.text_generation

:params:
:prompt (str) — Input text.

:details (bool, optional) — By default, text_generation returns a string. Pass details=True if you want a 

:detailed output (tokens, probabilities, seed, finish reason, etc.). Only available for models running on with the text-generation-inference backend.

:stream (bool, optional) — By default, text_generation returns the full generated text. Pass stream=True if you want a stream of tokens to be returned. Only available for models running on with the text-generation-inference backend.

:model (str, optional) — The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed Inference Endpoint. This parameter overrides the model defined at the instance level. Defaults to None.

:do_sample (bool) — Activate logits sampling

:max_new_tokens (int) — Maximum number of generated tokens

:best_of (int) — Generate best_of sequences and return the one if the highest token logprobs

:repetition_penalty (float) — The parameter for repetition penalty. 1.0 means no penalty. See this paper for more details.

:return_full_text (bool) — Whether to prepend the prompt to the generated text

:seed (int) — Random sampling seed

:stop_sequences (List[str]) — Stop generating tokens if a member of stop_sequences is generated

:temperature (float) — The value used to module the logits distribution.

:top_k (int) — The number of highest probability vocabulary tokens to keep for top-k-filtering.

:top_p (float) — If set to < 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation.

:truncate (int) — Truncate inputs tokens to the given size

:typical_p (float) — Typical Decoding mass See Typical Decoding for Natural Language Generation for more information

:watermark (bool) — Watermarking with A Watermark for Large Language Models

:decoder_input_details (bool) — Return the decoder input token logprobs and ids. You must set details=True as well for it to be taken into account. Defaults to False.

"""

client.text_generation(
    
)


"""
research agent
text-classification > action

https://huggingface.co/docs/huggingface_hub/v0.20.2/en/package_reference/inference_client#huggingface_hub.InferenceClient.text_classification

:params:
:text (str) — A string to be classified.

:model (str, optional) — The model to use for the text classification task. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed Inference Endpoint. If not provided, the default recommended text classification model will be used. Defaults to None.

"""
class Tool():
    def __init__(self):
        self
    
class Agent():
    def __init__(self):
        self
    
    def _evaluate_query():
        # Evaluate query to assign task
        return None
    
    def get_task():
        # some functcion    
        return None