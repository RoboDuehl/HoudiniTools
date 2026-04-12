import os 
import replicate 
from dotenv import load_dotenv
load_dotenv()  # finds HoudiniTools/.env automatically
print(os.getenv("REPLICATE_API_TOKEN"))

#pre_prompt = "You are Marie's loving boyfriend and hope she is doing well"
#usr_prompt = input("what is your questions Marie? ")

#response = replicate.run("a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
 #                       input={"prompt": f"{pre_prompt} {usr_prompt} AI: ", "repetition_penalty": 1}
                   #       )
#res = ""

import replicate

input = {
    "prompt": "Johnny has 8 billion parameters. His friend Tommy has 70 billion parameters. What does this mean when it comes to speed?",
    "max_new_tokens": 512,
    "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
}

for event in replicate.stream(
    "meta/meta-llama-3-8b-instruct",
    input=input
):
    print(event, end="")
#=> "The number of parameters in a neural network can impact ...
#=> "The number of parameters in a neural network can impact ...


#for r in response: 
 # res += r

#print(res)
