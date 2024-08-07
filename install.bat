Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install git
choco install python312
git clone https://github.com/OnyxAbove/auto-certificate.git
cd auto-certificate
pip3 install venv
python3 -m venv .venv
.venv\Scripts\activate.bat
pip3 install -r requirements.txt
