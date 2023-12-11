# mikeyTMNTchat
A chatbot that impersonates mikey from TMNT whom you can speak with using voice and responds in speech.
The script uses whisper for speech to text, llama.cpp python bindings for the chatbot and mozilla TTS for speaking back.

**Here are steps to install dependencies**

`pip install whisper-mic`

`CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python`

`pip install TTS`

`pip install -U "huggingface_hub[cli]"`

**The project uses mistral 7b model that can be downloaded using the command**

`huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF mistral-7b-instruct-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False`

