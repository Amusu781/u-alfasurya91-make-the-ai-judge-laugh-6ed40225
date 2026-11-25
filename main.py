"""Write one office-life joke to /output/entry.txt.

Deterministic: the same single line every run, no network, no env reads.
"""

import os

ENTRY = "The printer only jams on urgent documents, so now I mark everything 'not urgent'."


def main():
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path) and not os.path.islink(path):
            import shutil

            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
