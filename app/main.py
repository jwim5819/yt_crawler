import os
import subprocess
import shutil
import streamlink
import threading

from datetime import datetime

from app.config.settings import settings
from app.utils.logger import logger, print_line
from app.utils.chk_envs import (chk_envs)


def cleanup_files():
    current_time = datetime.now()
    for root, dirs, files in os.walk(settings.date_src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            time_difference = current_time - modified_time
            if time_difference.days >= settings.cleanup_cycle:
                os.remove(file_path)
    # cleanup 쓰레드 시작(하루에 한번 검사)
    threading.Timer(86400, cleanup_files).start()


def crawling_media():
    if settings.crawling_type == "video":
        file_ext = ".mp4"
    if settings.crawling_type == "audio":
        file_ext = ".wav"
    # 무한 루프
    while True:
        try:
            print_line()
            # 파일 이름 설정
            now = datetime.now()
            save_file_name = now.strftime("{}".format(settings.filename))
            tmp_file = os.path.normpath(os.path.join(settings.tmp_dir, save_file_name + file_ext))
            output_file = os.path.normpath(os.path.join(settings.save_dir, settings.date_src_dir, save_file_name + file_ext))

            # 경로가 없을 경우 생성
            os.makedirs(os.path.dirname(tmp_file), exist_ok=True)
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            # 로깅
            logger.info("Try to crawl media. URL: {}, Quality: {}, Output: {}".format(settings.target_url, settings.stream_quality, output_file))

            # Streamlink를 사용하여 실시간 스트리밍 가져오기
            streams = streamlink.streams(settings.target_url)
            stream = streams[settings.stream_quality]

            # 설정한 split_time마다 동영상 저장
            if settings.crawling_type == "video":
                subprocess.run(["ffmpeg", "-i", stream.url, "-t", str(settings.split_time), "-c", "copy", "-loglevel", "panic", tmp_file])
            if settings.crawling_type == "audio":
                subprocess.run(["ffmpeg", "-i", stream.url, "-t", str(settings.split_time), "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", "-loglevel", "panic", tmp_file])

            # 완전히 쓰기가 완료된 파일만 실제 경로로 이동
            shutil.move(tmp_file, output_file)

            # 로깅
            logger.info("Successfully crawled media. Output: {}".format(output_file))
        except (streamlink.exceptions.NoPluginError, streamlink.exceptions.StreamError):
            # 실시간 스트리밍 진행중이 아닐 경우
            logger.info("There is no live streaming now. Retry after {} seconds.".format(settings.split_time))
        except Exception as e:
            # 그 외 에러
            logger.error("An error occurred while crawling media. Error: {}".format(e))


def main():
    try:
        cleanup_files()
        # 환경 변수 출력
        logger.info("Crawler started.")
        print_line()
        for key, value in vars(settings).items():
            logger.info(f"{key}: {value}")  # 환경 변수 검사
        chk_envs()
        # 환경 변수가 유효하면 미디어 크롤링 시작
        crawling_media()
    except AssertionError as e:
        logger.error(str(e))
        return


if __name__ == "__main__":
    main()
