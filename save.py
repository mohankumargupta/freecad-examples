from pathlib import Path

def save_as(doc, fullpath):
    path = Path(fullpath)
    filename_without_extension = path.with_suffix("").name
    old = Path(f"{filename_without_extension}.FCStd")
    if old.exists():
        old.unlink()
    doc.saveAs(f"{filename_without_extension}.FCStd")
