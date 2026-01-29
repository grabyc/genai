##*** TO BE RUN FROM TERMINAL INSIDE PROJECT'S ROOT DIRECTORY ***##
python - <<'PY'
import asyncio
from agent import run_session, research_runner_compacting

# Turn 1
asyncio.run(run_session(
    research_runner_compacting,
    "What is the latest news about AI in healthcare?",
    "compaction_demo",
))

# Turn 2
asyncio.run(run_session(
    research_runner_compacting,
    "Are there any new developments in drug discovery?",
    "compaction_demo",
))

# Turn 3 - Compaction should trigger after this turn!
asyncio.run(run_session(
    research_runner_compacting,
    "Tell me more about the second development you found.",
    "compaction_demo",
))

# Turn 4
asyncio.run(run_session(
    research_runner_compacting,
    "Who are the main companies involved in that?",
    "compaction_demo",
))
PY

python - <<'PY'
import asyncio
from agent import run_session, research_runner_compacting, session_service, USER_ID

# Turn 1
asyncio.run(run_session(
    research_runner_compacting,
    "What is the latest news about AI in healthcare?",
    "compaction_demo",
))

# Turn 2
asyncio.run(run_session(
    research_runner_compacting,
    "Are there any new developments in drug discovery?",
    "compaction_demo",
))

# Turn 3 - Compaction should trigger after this turn!
asyncio.run(run_session(
    research_runner_compacting,
    "Tell me more about the second development you found.",
    "compaction_demo",
))

# Turn 4
asyncio.run(run_session(
    research_runner_compacting,
    "Who are the main companies involved in that?",
    "compaction_demo",
))

# Get the final session state
final_session = asyncio.run(session_service.get_session(
    app_name=research_runner_compacting.app_name,
    user_id=USER_ID,
    session_id="compaction_demo",
))

print("--- Searching for Compaction Summary Event ---")
found_summary = False
for event in final_session.events:
    # Compaction events have a 'compaction' attribute
    if event.actions and event.actions.compaction:
        print("\n✅ SUCCESS! Found the Compaction Event:")
        print(f"  Author: {event.author}")
        print(f"\n Compacted information: {event}")
        found_summary = True
        break

if not found_summary:
    print(
        "\n❌ No compaction event found. Try increasing the number of turns in the demo."
    )
PY

