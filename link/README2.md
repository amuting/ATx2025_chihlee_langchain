

## chocolatey install
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

## community.chocolatey
https://community.chocolatey.org/packages

## chocolatey git
https://community.chocolatey.org/packages/git
choco install git -y
rem choco install github-desktop -y
choco install cursoride -y
choco install ollama -y

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

## git conda
cli
gui

conda 可以建立虛擬環境
python
pip , 套件管理程式, pypi.org
perplexity ai
perplexity ai browser ,
perplexity ai agent ,

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


#uv README
https://github.com/roberthsu2003/python/tree/master/uv

#install uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

#UV COMMAND
uv --version

#UV VENV TEST
# 在已有的專案
uv init --python 3.10
uv venv

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

# 花蓮新聞10則