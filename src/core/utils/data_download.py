import wget


class Downloader:
    """
    Useful class to download files using wget command.

    Args:
        url: target file in URL, must be accessible. Type: str
    """

    def __init__(
        self,
        url: str,
    ) -> None:
        self.url = url

    def download_file(self) -> None:
        print(f"Downloading URL: {self.url}")
        wget.download(url=self.url)


if __name__ == "__main__":
    d = Downloader()
    print(d)
