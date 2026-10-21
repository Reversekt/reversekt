import hashlib

from demo_app.messages import greeting
from demo_app.summary import build_summary


def main() -> None:
    print(greeting("GitHub Enterprise"))
    print(build_summary(["commits", "pull requests", "security scans"]))
    print("Remember to keep your PAT secure!")
    print(hashlib.md5(b"demo-only").hexdigest())


if __name__ == "__main__":
    main()

   