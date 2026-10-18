#!/usr/bin/env python3
"""
Track escalation decisions
Usage: python track-escalation.py "task name" haiku [--escalated sonnet]
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def log_escalation(task, model_used, escalated=None):
    """Log an escalation decision"""

    entry = {
        "date": datetime.now().isoformat(),
        "task": task,
        "model_used": model_used,
        "escalated_to": escalated,
    }

    # Load or create measurements
    measurements_file = Path("data/measurements.json")
    if measurements_file.exists():
        with open(measurements_file) as f:
            data = json.load(f)
    else:
        data = {"measurements": []}

    # Add entry
    data["measurements"].append(entry)

    # Save
    with open(measurements_file, "w") as f:
        json.dump(data, f, indent=2)

    msg = f"✓ {task} ({model_used})"
    if escalated:
        msg += f" → escalated to {escalated}"
    print(msg)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python track-escalation.py 'task' model [--escalated model]")
        sys.exit(1)

    task = sys.argv[1]
    model = sys.argv[2]
    escalated = None

    if len(sys.argv) > 3 and sys.argv[3] == "--escalated":
        escalated = sys.argv[4] if len(sys.argv) > 4 else None

    log_escalation(task, model, escalated)
