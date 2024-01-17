from src.app.settings import DOWNLOAD_DIR, DOWNLOAD_FILENAME


class Downloader:
    """
    Useful class to download files using wget command.

    Args:
        url: target file in URL, must be accessible. Type: str
        filename: output filename of downloaded data. Will be concatenated in directory parameter. Type: str
        directory: output directory of downloaded data. Has a default value and will be concatenated with filename Type: [Path, str]
    """

    def __init__(
        self,
        url: str,
        filename=DOWNLOAD_FILENAME,
        directory=DOWNLOAD_DIR,
    ) -> None:
        self.url = url
        self.filename = filename
        self.directory = directory

    def get_output_filename(self):
        return self.directory.joinpath(self.filename)


if __name__ == "__main__":
    d = Downloader()
    print(d.get_output_filename())
