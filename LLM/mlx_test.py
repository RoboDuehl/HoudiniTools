from mlx_lm import load, generate

model, tokenizer = load("mistralai/Mistral-7B-v0.1")
usr_input = input("What is your question Marie ? ")
response = generate(model, tokenizer, prompt= usr_input, max_tokens=50, verbose = True)
