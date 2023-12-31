class DirectDownloadLinkException(Exception):
    """Not method found for extracting direct download link from the http link"""

    pass


class NotSupportedExtractionArchive(Exception):
    """The archive format use is trying to extract is not supported"""

    pass


class NotRclonePathFound(Exception):
    """Rclone path not found"""

    pass


class RssShutdownException(Exception):
    """This exception should be raised when shutdown is called to stop the montior"""

    pass


class ProviderException(Exception):
    def __init__(self, message, video_file_name):
        self.message = message
        self.video_file_name = video_file_name
        super().__init__(self.message)
