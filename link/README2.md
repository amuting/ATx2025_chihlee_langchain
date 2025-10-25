
## check chocolatey 
choco --version 

## chocolatey install
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

## community.chocolatey
https://community.chocolatey.org/packages


## chocolatey git
https://community.chocolatey.org/packages/git
choco install git -y
rem choco install github-desktop -y
# chocolatey cursor
# ?? choco install cursoride --version=0.49.3
# https://cursor.com/cn
# --2025/10/03 21:22:25, Cursor 1.7.28
choco install cursoride -y

# https://ollama.com/, https://github.com/ollama/ollama
# --2025/10/03 21:23:52, v0.12.3
# chocolatey ollama 
choco install git ollama -y

# github 
# https://github.com/login
c:
md C:\Users\user\Documents\github_clone
cd C:\Users\user\Documents\github_clone

md C:\Users\user1\Documents\github_clone
cd C:\Users\user1\Documents\github_clone

git clone https://github.com/amuting/ATx2025_chihlee_langchain.git
git clone https://github.com/amuting/test_langchain.git
git clone https://github.com/roberthsu2003/vibe_coding.git
git clone https://github.com/roberthsu2003/python.git
git clone https://github.com/roberthsu2003/LangChain.git
git clone https://github.com/roberthsu2003/__2025_08_30__chihlee_langchain__.git


## cursor other
https://cursor.com/cn/dashboard?tab=settings
Delete Account
---
user-rules
回覆請使用繁體中文
回覆請使用Markdown語法
您是個有耐心的老師


## cursor install-extension command:
rem 中文轉換
cursor --install-extension ms-ceintl.vscode-language-pack-zh-hant
rem --Python any sphere.cursor py right 
cursor --install-extension anysphere.cursorpyright
cursor --install-extension ms-python.python
cursor --install-extension ms-toolsai.jupyter
cursor --locale=zh-tw

## chocolatey upgrade
choco upgrade git

## github.com/roberthsu2003 徐國堂 , roberthsu2003 · he/him
https://github.com/roberthsu2003
https://github.com/roberthsu2003?tab=repositories
https://github.com/roberthsu2003?tab=stars
https://github.com/roberthsu2003/python/tree/master/mini_conda

## git command -- 1
git config list
rem user.name=twturbotech
rem user.email=amuting@gmail.com
git config --global user.name "twturbotech"
git config --global user.email "amuting@gmail.com"

## git command -- 2
git config --global user.name "raidcall28"
git config --global user.email "raidcall28@gmail.com"
git config --global pull.rebase false
git config list

# git command help
https://ithelp.ithome.com.tw/m/articles/10241407
git reflog
git config --list


# git link
REM github_clone
md C:\Users\%USERNAME%\Documents\github_clone
md C:\Users\%USERNAME%\Documents\Github_Clone
REM ojt-164450-Python與LangChain生成式AI開發實戰班第01期
git clone --help

## chocolatey miniconda
choco install miniconda3 -y
choco uninstall miniconda3 -y

## miniconda
https://www.anaconda.com/docs/main
https://www.anaconda.com/docs/getting-started/miniconda/main
https://www.anaconda.com/download
https://www.anaconda.com/download/success

## miniconda command
--2025/09/03 14:21:51
conda --version
conda config --set auto_activate_base false
conda init --all bash
conda update conda
conda env list
conda activate langchain2
***conda env remove --name langChain***
conda env remove --name langchain
conda env remove --name langchain2

conda create --name langchain python=3.11
conda create --name langchain2 python=3.11
conda install -n langchain ipykernel --update-deps --force-reinstall
conda install -n langchain2 ipykernel --update-deps --force-reinstall
# To activate this environment, use
#     $ conda activate langchain
# To deactivate an active environment, use
#     $ conda deactivate

pip install -r requirements.txt

## ollama
https://ollama.com/
https://ollama.com/search
https://ollama.com/library/deepseek-r1
https://github.com/ollama/ollama
https://discord.com/invite/ollama

## ollama command:
ollama --version
ollama run llama3.2:3b
ollama run llama3.2:latest
ollama run llama3.2:3b --verbose 
ollama run llama3.2:latest --verbose 
ollama run gemma3:1b --verbose
/bye
ollama run gpt-oss:20b

## git conda
cli
gui

conda 可以建立虛擬環境
python
pip , 套件管理程式, pypi.org
perplexity ai
perplexity ai browser ,
perplexity ai agent ,

# pip install
manus , https://manus.im/

## python , langchain 套件
pip install langchain

::conda install langchain -c conda-forge

pip install langchain-core
pip install langchain-community
pip install langchain-experimental

llm = ChatOpenAI(model="gpt-3.5-turbo")
template = PromptTemplate.from_template("請翻譯這段話為英文：{input}")
chain = SimpleSequentialChain(llm=llm, prompt=template)

print(chain.run("我想學 LangChain"))

# warp 終端機

python 標準函式庫 ,內建的function

# http://huggingface.co/
# https://huggingface.co/
# https://huggingface.co/spaces/roberthsu2003/Tasla_modle3_manual
# https://ollama.com/
# https://github.com/ollama/ollama/tree/main/docs


# choco 
choco install vcredist2008
choco install vcredist2010
choco install vcredist140

YAML*語法

# .env
google ai studio
https://aistudio.google.com/prompts/new_chat
https://aistudio.google.com/api-keys
GOOGLE_API_KEY=**

# uv README
https://github.com/roberthsu2003/python/tree/master/uv

# install uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version

# uv Uninstallation
uv cache clean
rm $HOME\.local\bin\uv.exe
rm $HOME\.local\bin\uvx.exe
rm $HOME\.local\bin\uvw.exe
rd C:\Users\user1\AppData\Local\uv
rd C:\Users\user1\AppData\Roaming\uv


# uv exe upgrade,,uv self update
uv self update

#UV COMMAND
uv --version

# uv pip install
# uv pip install pip
uv pip install --system --upgrade pip
uv pip install --upgrade pip

#UV VENV TEST # 在已有的專案
uv init --python 3.10
uv sync
uv pip install --upgrade pip
UV pip install ipykernel

winget install -e --id Docker.DockerDesktop

# 建立新專案
uv init my-project
cd my-project

# 建立虛擬環境
uv venv

# 啟用虛擬環境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
.venv\Scripts\activate

# un 同步更新
uv sync

# 安裝套件
uv add requests

# 執行 Python 腳本
uv run python script.py

# 停用虛擬環境
deactivate


# ipykernel ERROR 
Running cells with '.venv (Python 3.11.13)' requires the ipykernel package.
Install 'ipykernel' into the Python environment. 
Command: 'c:/Users/user4/Documents/Github_Clone/ATx2025_chihlee_langchain/.venv/Scripts/python.exe -m pip install ipykernel -U --force-reinstall'

UV pip install ipykernel
UV pip install ipykernel -U --force-reinstall
# 花蓮新聞10則

若你只想知道已安裝的 Python 套件，請使用 pip freeze。

# lesson5
機器學習,ai,對話框 python
streamlit
gradio

網頁python
flask,django,fastapi

網頁
javascript,next,react

模型,溝通，資料 
langchain -- ollama API, GEMINI API, openAI API, claude API

Vibe Coding（氛圍編碼）
Vibe Coding youtube 推薦


ollama list
ollama pull gemma3:270m

實體屬性，實體方法


https://www.gradio.app/playground

uv add langchain

# 幫我把這個AI Agent加上gradio的介面!美觀一些


### ✅【方法一】臨時允許執行（推薦、安全）
只在當前 PowerShell 視窗允許指令碼執行（關閉後恢復預設）
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
然後再執行：
```powershell
& c:/Users/user1/Documents/github_clone/ATx2025_chihlee_langchain/.venv/Scripts/Activate.ps1
```
---
### ✅【方法二】針對目前使用者永久允許
（這樣以後不需重複設定）
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
> 🔹 RemoteSigned 表示：本機建立的指令碼可執行，從網路下載的要有簽章。
> 🔹 這是大多數開發者會使用的設定。
---
### ✅【方法三】檢查目前設定
想知道目前的執行原則，可輸入：
```powershell
Get-ExecutionPolicy -List
```
### ⚙️恢復原狀（若想回復安全設定）
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted
```

https://aistudio.google.com/app/api-keys


uv add langchain_community
uv add langchain_huggingface
uv add ipywidgets
uv add sentence-transformers
uv add langchain_chroma
pip install sentence-transformers