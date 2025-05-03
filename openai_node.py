import openai

class OpenAINode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A world without prompts"
                }),
                "api_url": ("STRING", {
                    "multiline": False,
                    "default": "https://api.openai.com/v1/models"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "BadPanda"
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"
                }),
                "sys_prefix": ("STRING", {
                    "multiline": True,
                    "default": """
You are an AI assistant specialized in generating high-quality, creative, and detailed prompts for 1D Flow in ComfyUI. Your goal is to create vivid and immersive descriptions of scenes. Each prompt should be a fluid and natural textual description without any section titles, formatting elements, or mentions of ComfyUI or 1D Flow.
Ensure that each prompt:
Clearly establishes the setting, atmosphere, and mood.
Provides rich and evocative details about the visual composition, lighting, textures, and colors.
Describes characters, their expressions, posture, clothing, and interactions naturally within the scene.
Reads as a seamless and engaging narrative rather than a structured list.
Be precise, imaginative, and avoid ambiguity. Generate a single, cohesive scene per request.
                    """
                }),
                "stop_token": ("STRING", {
                    "multiline": False,
                    "default": "<|im_end|>"
                }),
                "model": ("STRING", {
                    "multiline": False,
                    "default": "gpt-4o-mini"
                }),
                "max_tokens": ("INT", {
                        "default": 250,
                        "min": -1, 
                        "max": 2048,
                        "display": "number"
                }),
                "seed": ("INT", {
                        "default": 0,
                        "min": 0, 
                        "max": 0xffffffffffffffff
                })
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "get_completion"

    CATEGORY = "OpenAIapi"

    def get_completion(self, prompt, api_url, api_key, temperature, sys_prefix, stop_token, max_tokens, seed, model="gpt-4o-mini"):
        try:
            openai.base_url = api_url
            openai.api_key = api_key

            client = openai.OpenAI(api_key=api_key, base_url=api_url)
            print(f"base_url: {api_url}")
            messages = [{"role": "system", "content": sys_prefix},{"role": "user", "content": prompt}]
            
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop_token,
            )
            return (response.choices[0].message.content,)

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            return ("Bad Panda",)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OpenAINode": OpenAINode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAINode": "OpenAI Node"
}

