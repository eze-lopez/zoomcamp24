"""General settings for app, such as ROOT_DIR, DOWNLOAD_DIR and other helpers"""

from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent.parent
DOWNLOAD_DIR = ROOT_DIR.joinpath(".temp_data/")

if __name__ == "__main__":
    print("GENERAL APP SETTINGS:")
    print(f"\tROOT_DIR: {ROOT_DIR}")
    print(f"\tDOWNLOAD_DIR: {DOWNLOAD_DIR}")
