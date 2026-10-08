# LocalMind Robotics - Simulator Setup

This guide explains how to run the Reachy Mini simulator with our local Qwen AI setup.

## 1. Clone the repository

```powershell
git clone https://github.com/LoanT7/LocalMind-Robotics-Reachy-Mini-Capstone.git

cd LocalMind-Robotics-Reachy-Mini-Capstone

##2. Create virtual env
py -3.13 -m venv .venv

Activate it:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

##3 Install Python Packages 
python -m pip install -r requirements.txt

##4 Start the Reachy Mini simulator
Open the Reachy Mini desktop application.
Select:
Simulation → Start
Leave the simulator running.

##5. Install llama.cpp
winget install llama.cpp

Close and reopen the terminal after installation.

##6. Start the local Qwen model
llama-server -hf Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q4_K_M

Leave this terminal running.
The local AI server will run at:
http://localhost:8080

##7. Run the Reachy AI simulator program
Open another terminal.
Activate the virtual environment again:
.\.venv\Scripts\Activate.ps1

Run:
python src\simulator\reachy_qwen_test.py

Current Working Flow
User types a message
→ Local Qwen AI
→ AI response
→ Text-to-speech
→ Reachy Mini simulator movement
Next Step
The next goal is to add speech-to-text so the user can speak to Reachy instead of typing.
