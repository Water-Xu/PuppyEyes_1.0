import cv2
import subprocess

def stream_to_rtmp (stream_path, video_speed):
    print(stream_path)
    output_rtmp = 'rtmp://localhost:1935/hls_cam/detect'#推流地址

    fps = 24#帧率
    # -loglevel quiet/info
    ffmpeg_cmd = (
        "/usr/local/Cellar/ffmpeg/6.0_1/bin/ffmpeg "
        "-y -loglevel quiet  -re -i "
        f"{stream_path} "
        "-vf \"setpts="
        f"{video_speed}*PTS\" "
        "-c:v libx264 -b:v 500k -preset veryfast -f flv -r "
        f"{fps} "
        f"{output_rtmp}"
    )

    # 启动 ffmpeg 进程
    p = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, shell=True)

    p.communicate()

