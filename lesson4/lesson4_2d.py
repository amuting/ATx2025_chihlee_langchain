# from langchain_ollama import ChatOllama
import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# 載入環境變數, 載入.env,模擬電腦環境變數
load_dotenv()


# 使用最原始的呼叫方式：直接以字串 prompt 送到 Ollama
# model = ChatOllama(model="llama3.2:latest", base_url="http://localhost:11434")

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def answer(prompt: str) -> str:
    """最簡單的 wrapper：把 prompt 傳給 model.invoke，回傳文字回應。"""
    if not prompt:
        return ""
    res = model.invoke(prompt)
    return res.content if hasattr(res, "content") else str(res)


# 最小的 Gradio 介面：一個輸入框 + 一個文字輸出
iface = gr.Interface(
    fn=answer,
    inputs=gr.Textbox(lines=3, placeholder="在此輸入問題，按送出..."),
    outputs=gr.Textbox(lines=3),
    title="ChatGoogleGenerativeAI 簡易 Gradio 範例",
    description="示範如何把原先的 ChatGoogleGenerativeAI 呼叫整合到 Gradio。",
)

if __name__ == "__main__":
    iface.launch(server_name="127.0.0.1", server_port=7860)
