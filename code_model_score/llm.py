from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen2.5-Coder-14B-Instruct",
          gpu_memory_utilization=.9,
          max_model_len=8192)
sampling_params = SamplingParams(temperature=0.9,
                                 max_tokens=10000)


def messages_to_prompt(messages):
    
    if isinstance(messages, str):
        # If message is already a string, return it directly
        return messages
    prompt = ""
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        prompt += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"  # prompt the model to respond
    return prompt


def vllm_server(message):
    message = messages_to_prompt(message)
    outputs = llm.generate(message, sampling_params)
    result = outputs[0].outputs[0].text
    return result


# test code
'''
def main():
        result = vllm_server('Introduce yourself')
        print(result)

if __name__ == "__main__":
    main()

'''
