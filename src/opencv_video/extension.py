from enum import Enum   

class VideoExtension(Enum):
    """
    VideoExtension is the extension for the video.

    Attributes:
    ----------
    MP4: The MP4 extension.
    AVI: The AVI extension.
    MKV: The MKV extension.
    MOV: The MOV extension.
    """
    MP4 = "mp4"
    AVI = "avi"
    MKV = "mkv"
    MOV = "mov"
    # WEBM = "webm"
    # FLV = "flv"
    # WMV = "wmv"
    # MPEG = "mpeg"
    # MPG = "mpg"
    # M4V = "m4v"

    @property
    def list_extensions(self) -> list[str]:
        return [ext.value for ext in type(self)]
