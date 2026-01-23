fastAPI basics for quick deployment of projects, might come handy some day

### How to Run the Programs!
```bash
python -m venv .venv
source .venv/bin/activate.fish #i am a fish user
pip install fastapi uvicorn
unvicorn api:app --reload       #api is the file name and app is app created in the program, --reload makes it easy to see realtime changes in your code taking action
```
things i liked about fastAPI
- very easy to start
- minimal python knowledge required
- best for quick deployment of prototypes or even bigger projects
