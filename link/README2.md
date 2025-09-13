

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
conda env remove --name langChain 
conda env remove --name langchain
conda create --name langchain python=3.11
conda create --name langchain2 python=3.11
conda install -n langchain ipykernel --update-deps --force-reinstall
conda install -n langchain2 ipykernel --update-deps --force-reinstall
# To activate this environment, use
#     $ conda activate langchain
# To deactivate an active environment, use
#     $ conda deactivate

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
/bye
