from pathlib import Path

from src.helper.timer import DownloadTimer


class Downloader:
    def __init__(self, path: str | Path, timeout: int = 60, rename: str = None):
        """
        path: file path
        timeout: sec
        rename: rename to file_name,  file_name should contains suffix
        """
        self._path = Path(path)
        self._timeout = timeout
        self._rename = rename
        self._target_path = None
        self._timer = DownloadTimer(path, timeout)

        if rename:
            self._target_path = self._path.parent / rename

    def start(self):
        self._timer.start()
        if self._target_path.is_file():
            self._target_path.unlink()
        self._path.rename(self._target_path)
