import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# 初始化模型
model = OllamaLLM(model="llama3.2:latest")

# 建立多變數的翻譯模板
complex_template = """
你是一位專業的{target_language}翻譯家，專精於{domain}領域。
請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣和風格
2. 使用專業術語
3. 符合{target_language}的語言習慣

{source_language}文本：{text}
{target_language}翻譯：
"""

chat_prompt_template = ChatPromptTemplate.from_template(complex_template)

def translate_text(source_text, source_language, target_language, domain):
    """
    翻譯功能
    """
    if not source_text.strip():
        return "請輸入要翻譯的文本！"
    
    try:
        # 格式化提示詞
        formatted_prompt = chat_prompt_template.format(
            target_language=target_language,
            source_language=source_language,
            domain=domain,
            text=source_text
        )
        
        # 調用模型進行翻譯
        response = model.invoke(formatted_prompt)
        return response
        
    except Exception as e:
        return f"翻譯過程中發生錯誤：{str(e)}"

# 創建Gradio介面
def create_interface():
    with gr.Blocks(
        title="AI專業翻譯助手",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            max-width: 1200px !important;
            margin: auto !important;
        }
        .header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .translation-box {
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            padding: 15px;
            background-color: #f8f9fa;
        }
        """
    ) as interface:
        
        # 標題區域
        gr.HTML("""
        <div class="header">
            <h1>🤖 AI專業翻譯助手</h1>
            <p>使用先進的語言模型進行專業翻譯，支援多種語言和專業領域</p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                # 輸入區域
                gr.Markdown("### 📝 翻譯設定")
                
                source_language = gr.Dropdown(
                    choices=["英文", "日文", "韓文", "法文", "德文", "西班牙文", "義大利文", "俄文"],
                    value="英文",
                    label="源語言",
                    info="選擇要翻譯的原始語言"
                )
                
                target_language = gr.Dropdown(
                    choices=["繁體中文", "簡體中文", "英文", "日文", "韓文", "法文", "德文", "西班牙文"],
                    value="繁體中文",
                    label="目標語言",
                    info="選擇翻譯後的目標語言"
                )
                
                domain = gr.Dropdown(
                    choices=["商業", "科技", "醫學", "法律", "教育", "文學", "新聞", "一般"],
                    value="商業",
                    label="專業領域",
                    info="選擇翻譯的專業領域"
                )
                
                source_text = gr.Textbox(
                    label="要翻譯的文本",
                    placeholder="請輸入要翻譯的文本...",
                    lines=8,
                    max_lines=15,
                    info="支援長文本翻譯"
                )
                
                translate_btn = gr.Button(
                    "🚀 開始翻譯",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                # 輸出區域
                gr.Markdown("### 🌟 翻譯結果")
                
                with gr.Group():
                    result_text = gr.Textbox(
                        label="翻譯結果",
                        lines=8,
                        max_lines=15,
                        interactive=False,
                        elem_classes=["translation-box"]
                    )
                
                # 操作按鈕
                with gr.Row():
                    clear_btn = gr.Button("🗑️ 清除", variant="secondary")
                    copy_btn = gr.Button("📋 複製結果", variant="secondary")
        
        # 範例區域
        with gr.Accordion("💡 使用範例", open=False):
            gr.Markdown("""
            **商業範例：**
            - 英文 → 繁體中文：`The quarterly revenue increased by 15% compared to last year.`
            
            **科技範例：**
            - 英文 → 繁體中文：`Machine learning algorithms can process large datasets efficiently.`
            
            **醫學範例：**
            - 英文 → 繁體中文：`The patient shows signs of improvement after the treatment.`
            """)
        
        # 事件綁定
        translate_btn.click(
            fn=translate_text,
            inputs=[source_text, source_language, target_language, domain],
            outputs=result_text
        )
        
        clear_btn.click(
            fn=lambda: ("", ""),
            outputs=[source_text, result_text]
        )
        
        copy_btn.click(
            fn=lambda x: x,
            inputs=result_text,
            outputs=gr.Clipboard()
        )
        
        # 頁腳
        gr.HTML("""
        <div style="text-align: center; padding: 20px; color: #666;">
            <p>Powered by LangChain + Ollama | 支援多種語言模型</p>
        </div>
        """)
    
    return interface

# 啟動應用程式
if __name__ == "__main__":
    interface = create_interface()
    interface.launch(
        server_name="localhost",
        server_port=7860,
        share=False,
        show_error=True,
        show_tips=True
    )