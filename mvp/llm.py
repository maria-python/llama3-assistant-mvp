import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

MODEL_DIR = "models/meta-llama-3-8B"

tokenizer = LlamaTokenizer.from_pretrained(MODEL_DIR, use_fast=False)
model = LlamaForCausalLM.from_pretrained(
    MODEL_DIR,
    torch_dtype=torch.float32
)

def chat_with_llm(messages: list) -> str:
    conversation = ""
    for msg in messages:
        conversation += f"[{msg['role'].upper()}]: {msg['content']}\n"

    inputs = tokenizer(conversation, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return only new generated part if possible
    return generated_text[len(conversation):].strip()