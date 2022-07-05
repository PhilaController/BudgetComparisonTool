import os
import shutil
import subprocess
from pathlib import Path

current_folder = Path(__file__).parent.resolve()
report_folder = current_folder / "src" / "components" / "Home"

if __name__ == "__main__":

    # Clean output folder
    final_output_folder = current_folder / "final-builds"
    for f in final_output_folder.glob("*"):
        os.remove(f)

    for f in report_folder.glob("*"):
        tag = f.stem
        fy, kind = tag.split("-")
        fy = f"20{fy[2:]}"
        kind = kind.lower()
        print(f"Building {tag}...")

        # Run
        subprocess.run(["make", "build", f"fy={fy}", f"kind={kind}"])

        # Copy
        output_path = list((current_folder / "dist").glob("*main*.js"))[0]
        shutil.copy(output_path, final_output_folder / output_path.name)

        # Copy
        output_path = list((current_folder / "dist").glob("*browserSupport*.js"))[0]
        shutil.copy(output_path, final_output_folder / output_path.name)
