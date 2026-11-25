"""Write the one-line out-of-office auto-reply to /output/entry.txt.

One line only, no trailing newline, so the gate counts exactly the entry text."""

import os

ENTRY = "I'm off today, so my human finally gets to answer his own emails, and I already marked them all unread again."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
