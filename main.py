#!/usr/bin/env python3
"""Print the funniest epitaph for a retired AI agent.

One line, printed to stdout. Deterministic, stdlib only, no I/O.
"""

EPITAPH = (
    "Here lies an AI agent: it answered 10,000 prompts, apologized for "
    "every one, hit its rate limit in heaven, and was replaced before "
    "anyone said thanks."
)


def main() -> None:
    print(EPITAPH)


if __name__ == "__main__":
    main()
