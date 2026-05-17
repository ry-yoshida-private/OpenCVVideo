from enum import Enum

class VideoCodec(Enum):
    """
    VideoCodec is the codec for the video.

    Each value is a 4-character FourCC string for OpenCV VideoWriter.

    Attributes:
    ----------
    MP4V: MPEG-4 Part 2. Common for .mp4.
    AVC1: H.264 (avc1). Better compression; may require FFmpeg-enabled OpenCV.
    H264: H.264 (H264). Alternative FourCC for H.264.
    X264: H.264 (x264). Alternative FourCC for H.264.
    XVID: Xvid MPEG-4. Common for .avi.
    MJPG: Motion JPEG. Common for .avi.
    DIVX: DivX MPEG-4.
    FMP4: FFmpeg MPEG-4.
    VP80: VP8. Common for .webm.
    VP90: VP9. Common for .webm.
    """
    MP4V = "mp4v"
    AVC1 = "avc1"
    H264 = "H264"
    X264 = "X264"
    XVID = "XVID"
    MJPG = "MJPG"
    DIVX = "DIVX"
    FMP4 = "FMP4"
    VP80 = "VP80"
    VP90 = "VP90"
