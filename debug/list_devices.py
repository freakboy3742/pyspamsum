import json
import pprint
import subprocess

try:
    raw_json = subprocess.check_output(
        ["xcrun", "simctl", "--set", "testing", "list", "-j"]
    )
    json_data = json.loads(raw_json)
    pprint.pprint(json_data)
    print(
        "simulators",
        [
            simulator
            for runtime, simulators in json_data["devices"].items()
            for simulator in simulators
            if (runtime.split(".")[-1].startswith("iOS") and simulator["isAvailable"])
        ],
    )
    print(
        "booted",
        [
            simulator["udid"]
            for runtime, simulators in json_data["devices"].items()
            for simulator in simulators
            if (
                runtime.split(".")[-1].startswith("iOS")
                and simulator["state"] == "Booted"
                and simulator["isAvailable"]
            )
        ],
    )
except subprocess.CalledProcessError as e:
    if e.returncode == 1:
        print("Error, but no simulators")
    else:
        raise
