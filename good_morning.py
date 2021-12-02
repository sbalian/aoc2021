#!/usr/bin/env python

import os

TEMPLATE = """\
#!/usr/bin/env python


def main():
    print("All tests passed.")


if __name__ == "__main__":
    main()
"""


def main():
    try:
        day = (
            max(
                [
                    int(item[3:])
                    for item in os.listdir(".")
                    if item.startswith("day")
                ]
            )
            + 1
        )
    except ValueError:
        day = 1
    dir_name = f"day{day}"
    os.mkdir(dir_name)
    file_name = f"./{dir_name}/{dir_name}.py"
    with open(file_name, "w") as f:
        f.write(TEMPLATE)
    os.system(f"chmod +x {file_name}")
    os.system(f"touch ./{dir_name}/input.txt")


if __name__ == "__main__":
    main()
