##*** TO BE RUN FROM TERMINAL INSIDE PROJECT'S ROOT DIRECTORY ***##

## Testing Session State in Action
python - <<'PY'
import asyncio
from agent import run_session, runner

asyncio.run(run_session(
    runner,
    [
        "Hi there, how are you doing today? What is my name?",  # Agent shouldn't know the name yet
        "My name is Sam. I'm from Poland.",  # Provide name - agent should save it
        "What is my name? Which country am I from?",  # Agent should recall from session state
    ],
    "state-demo-session",
))
PY

## Inspecting Session State
python - <<'PY'
import asyncio
from agent import run_session, runner, session_service, APP_NAME, USER_ID

asyncio.run(run_session(
    runner,
    [
        "Hi there, how are you doing today? What is my name?",  # Agent shouldn't know the name yet
        "My name is Sam. I'm from Poland.",  # Provide name - agent should save it
        "What is my name? Which country am I from?",  # Agent should recall from session state
    ],
    "state-demo-session",
))

# Retrieve the session and inspect its state
session = asyncio.run(session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id="state-demo-session"
))

print("Session State Contents:")
print(session.state)
print("\n🔍 Notice the 'user:name' and 'user:country' keys storing our data!")
PY

## Session State Isolation and Cross-Session State Sharing
python - <<'PY'
import asyncio
from agent import run_session, runner, session_service, APP_NAME, USER_ID

asyncio.run(run_session(
    runner,
    [
        "Hi there, how are you doing today? What is my name?",  # Agent shouldn't know the name yet
        "My name is Sam. I'm from Poland.",  # Provide name - agent should save it
        "What is my name? Which country am I from?",  # Agent should recall from session state
    ],
    "state-demo-session",
))

asyncio.run(run_session(
    runner,
    ["Hi there, how are you doing today? What is my name?"],
    "new-isolated-session",
))

# Check the state of the new session
session = asyncio.run(session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id="new-isolated-session"
))

print("New Session State:")
print(session.state)
PY
