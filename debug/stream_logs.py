import subprocess
import sys

udid = sys.argv[1]
print("streaming", udid)
subprocess.run(
    [
        "xcrun",
        "simctl",
        "--set",
        "testing",
        "spawn",
        udid,
        "log",
        "stream",
        "--style",
        "compact",
        "--predicate",
        'senderImagePath ENDSWITH "/iOSTestbedTests.xctest/iOSTestbedTests"'
        ' OR senderImagePath ENDSWITH "/Python.framework/Python"',
    ]
)
