__version__ = "0.2.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import subprocess
import sys


def format_crystal(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode()
    subprocess_kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.DEVNULL,
        "input": unformatted_bytes,
    }

    for cmd in (
        ["crystal", "tool", "format", "-"],
        ["docker", "run", "-i", "--rm", "crystallang/crystal:latest", "crystal", "tool", "format", "-"],
        ["podman", "run", "-i", "--rm", "docker.io/crystallang/crystal:latest", "crystal", "tool", "format", "-"],
    ):
        try:
            result = subprocess.run(cmd, **subprocess_kwargs)
            break
        except FileNotFoundError:
            pass
    else:
        raise Exception("No crystal executable found")

    if result.returncode:
        raise Exception("Failed to format crystal code")
    return result.stdout.decode()
