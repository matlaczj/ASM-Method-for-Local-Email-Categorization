{
  "name": "ehartford_dolphin-2.0-mistral-7b",
  "arch": "llama",
  "quant": "Q6_K",
  "context_length": 32768,
  "embedding_length": 4096,
  "num_layers": 32,
  "rope": {
    "freq_base": 10000,
    "dimension_count": 128
  },
  "head_count": 32,
  "head_count_kv": 8,
  "parameters": "7B"
}

{
  "name": "teknium_openhermes-2.5-mistral-7b",
  "arch": "llama",
  "quant": "Q6_K",
  "context_length": 32768,
  "embedding_length": 4096,
  "num_layers": 32,
  "rope": {
    "freq_base": 10000,
    "dimension_count": 128
  },
  "head_count": 32,
  "head_count_kv": 8,
  "parameters": "7B"
}

{
  "name": "Phi2",
  "arch": "phi2",
  "quant": "Q6_K",
  "context_length": 2048,
  "embedding_length": 2560,
  "num_layers": 32,
  "rope": {
    "dimension_count": 32
  },
  "head_count": 32,
  "head_count_kv": 32,
  "parameters": "3B"
}

{
  "name": "mistralai_mistral-7b-instruct-v0.2",
  "arch": "llama",
  "quant": "Q6_K",
  "context_length": 32768,
  "embedding_length": 4096,
  "num_layers": 32,
  "rope": {
    "freq_base": 1000000,
    "dimension_count": 128
  },
  "head_count": 32,
  "head_count_kv": 8,
  "parameters": "7B"
}

{
  "name": "open-orca_mistral-7b-openorca",
  "arch": "llama",
  "quant": "Q6_K",
  "context_length": 32768,
  "embedding_length": 4096,
  "num_layers": 32,
  "rope": {
    "freq_base": 10000,
    "dimension_count": 128
  },
  "head_count": 32,
  "head_count_kv": 8,
  "parameters": "7B"
}


| Model Name                                | Architecture | Quantization | Context Length | Embedding Length | Number of Layers | Rope Parameters                   | Head Count | Head Count (KV) | Parameters |
|-------------------------------------------|--------------|--------------|----------------|------------------|-------------------|-----------------------------------|------------|-----------------|------------|
| ehartford_dolphin-2.0-mistral-7b          | llama        | Q6_K         | 32768          | 4096             | 32                | Freq Base: 10000, Dim Count: 128   | 32         | 8               | 7B         |
| teknium_openhermes-2.5-mistral-7b          | llama        | Q6_K         | 32768          | 4096             | 32                | Freq Base: 10000, Dim Count: 128   | 32         | 8               | 7B         |
| Phi2                                      | phi2         | Q6_K         | 2048           | 2560             | 32                | Dim Count: 32                     | 32         | 32              | 3B         |
| mistralai_mistral-7b-instruct-v0.2        | llama        | Q6_K         | 32768          | 4096             | 32                | Freq Base: 1000000, Dim Count: 128 | 32         | 8               | 7B         |
| open-orca_mistral-7b-openorca             | llama        | Q6_K         | 32768          | 4096             | 32                | Freq Base: 10000, Dim Count: 128   | 32         | 8               | 7B         |

