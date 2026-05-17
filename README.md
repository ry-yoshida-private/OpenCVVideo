# OpenCVVideo

`OpenCVVideo` provides Python utilities for reading and writing video with OpenCV. It includes `VideoReader` for efficient frame iteration and extraction, and `VideoWriter` for creating videos from images with optional frame timestamps.

## Installation

From the project root:

```bash
pip install -e .
```

Or install dependencies only (use when developing without installing the package):

```bash
pip install -r requirements.txt
```

## Usage

### VideoReader

```python
from opencv_video import VideoReader
import cv2

video_path = "your_video.mp4"
reader = VideoReader(video_path)

print(f"Total frames: {len(reader)}")

for i, frame in enumerate(reader):
    if i == 5:
        cv2.imwrite("frame_0005.jpg", frame)
    if i >= 10:
        break

frame_100 = reader.extract_frame(100)
if frame_100 is not None:
    cv2.imwrite("frame_0100.jpg", frame_100)

with VideoReader(video_path, iter_start_frame=10, freq=5) as custom_reader:
    for i, frame in enumerate(custom_reader):
        if i == 2:
            cv2.imwrite("custom_frame_0002.jpg", frame)
        if i >= 5:
            break
```

### VideoWriter

```python
import cv2
import numpy as np
from opencv_video import VideoWriter, VideoWriterParameters
from opencv_video.codec import VideoCodec

params = VideoWriterParameters(fps=30, codec=VideoCodec.MP4V)

with VideoWriter("output.mp4", params) as writer:
    for _ in range(100):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        writer.write(frame)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
