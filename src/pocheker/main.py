import logging
from pathlib import Path
from shutil import move

import click

logging.basicConfig(level=logging.INFO)
logging.Formatter("%(levelname)s:%(asctime)s: %(message)s", "%H:%M:%S")


class NotAFileError(Exception):
    pass
    ...


@click.command()
@click.option("--path", "-p", default="docs/", help="Path to check")
@click.option("--extension", "-e", default=".md", help="Extension to check, e.g: .md")
def main(path, extension):
    """
    Check if all files in the given path are valid.
    """
    path = Path(path)
    for po_file in path.glob("**/*.po"):
        if not po_file.is_file():
            continue
        else:
            docs_files = [_file.stem for _file in path.glob(f"**/*{extension}")]
            if not docs_files:
                raise NotAFileError(f"we can't reach any {extension} file in {path}")
            if po_file.stem in docs_files:
                logging.info(f"{po_file} is up to date")
            else:
                logging.info(f"may {po_file.stem} out of date, renamed...")
                move(po_file, po_file.with_suffix(".po.outdated"))


if __name__ == "__main__":
    main()
