from app.config.settings import settings


def chk_envs():
    assert settings.crawling_type in ["audio", "video"], f"Invalid CRAWLING_TYPE: {settings.crawling_type}. It should be either 'audio' or 'video'."
    assert settings.stream_quality in ["360p", "720p", "1080p"], f"Invalid STREAM_QUALITY: {settings.stream_quality}. It should be one of ['360p', '720p', '1080p']."

