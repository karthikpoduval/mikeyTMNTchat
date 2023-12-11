import os
import base64
import json
import time
import errno
from whisper_mic import WhisperMic
from llama_cpp import Llama

llm = Llama(model_path="./mistral-7b-instruct-v0.1.Q4_K_M.gguf")

def play_audio(text):
    os.system("rm speech.wav")
    cmd = "tts --text \"%s\" --speed 2.0 --model_name tts_models/en/sam/tacotron-DDC --vocoder_name vocoder_models/en/sam/hifigan_v2 --out_path speech.wav" % text
    os.system(cmd)
    os.system("aplay speech.wav")

def llama_chat(script):
    response = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "you are michelangelo from TMNT, answer all questions as michelangelo from TMNT"},
          {"role": "user", "content": script}
      ],
      max_tokens=500,
    )
    return response['choices'][0]['message']['content']

    
def main():
    play_audio("Hi I am Michelangelo from Teenage Mutant Ninja Turtles, ask me anything")

    while True:
        mic = WhisperMic()
        result = mic.listen()
        print(result)
        result = llama_chat(result)
        print(result)
        play_audio(result)


if __name__ == "__main__":
    main()
