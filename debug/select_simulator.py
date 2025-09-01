import json
import subprocess

raw_json = subprocess.check_output(["xcrun", "simctl", "list", "-j"])
json_data = json.loads(raw_json)
se_simulators = sorted(
    (devicetype["minRuntimeVersion"], devicetype["name"])
    for devicetype in json_data["devicetypes"]
    if devicetype["productFamily"] == "iPhone"
    and (
        ("iPhone " in devicetype["name"] and devicetype["name"].endswith("e"))
        or "iPhone SE " in devicetype["name"]
    )
)

device_name = se_simulators[-1][1]
print(f"{device_name=}")
