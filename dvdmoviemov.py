import os
from pathlib import Path

VIDEO_PATH = Path("./VIDEO_TS").absolute()


def main():
    video_Export_Path = "ExportedMp4Videos"
    if os.path.isdir(video_Export_Path) is False:
        os.mkdir(video_Export_Path)

    for i in os.listdir(path=VIDEO_PATH):
        file_obj = Path(i)
        if file_obj.suffix == ".VOB":
            name = file_obj.name.split(".")[0]
            print(name)
            ffmpegCommand = (
                f"ffmpeg -i ./VIDEO_TS/{i} ./{video_Export_Path}/{name}.mov -crf 14"
            )
            os.system(ffmpegCommand)


if __name__ == "__main__":
    main()
