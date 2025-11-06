# Simple Login + Visit Counter (Flask)

Two users (`user1/pass1`, `user2/pass2`). After login, the dashboard shows how many times that user has visited.

## Run locally

```bash
# 1) Create & activate a virtual environment
python -m venv .venv
# Windows:
#   .venv\Scripts\activate
# macOS/Linux:
#   source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run
python app.py
# open http://127.0.0.1:5000
