"""Six Words, One Story — writes one six-word story to entry.txt."""

import os

STORY = "She wrote his eulogy. He proofread."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
