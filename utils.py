import openai


def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Image generating prompt generator. Who generates random text prompts to generate an AI Image in stable diffusion and Dall-e separatly."},
        {"role": "user", "content": "I want to get 5 prompts to generate an Image in stable diffution and Dall-e."},
        {"role": "assistant", "content": "That's awesome, I can generate some amazing and cool prompts for you to generate some great images in Stable Diffusion and Dall-e. Tell me a topic and I get you amazing prompts in tablular format."}
    ]
    return messages

