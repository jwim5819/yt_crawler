import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    target_url: str = os.getenv("TARGET_URL")
    tmp_dir: str = os.getenv("TMP_DIR")
    save_dir: str = os.getenv("SAVE_DIR")
    filename: str = os.getenv("FILENAME", default="streaming-%Y-%m-%d_%H_%M_%S")
    stream_quality: str = os.getenv("STREAM_QUALITY", default="1080p")
    crawling_type: str = os.getenv("CRAWLING_TYPE")
    split_time: int = os.getenv("SPLIT_TIME")
    data_src_l_cd: str = os.getenv("DATA_SRC_L_CD")
    data_src_m_cd: str = os.getenv("DATA_SRC_M_CD")
    data_src_s_cd: str = os.getenv("DATA_SRC_S_CD")
    date_src_dir: str = os.path.join(data_src_l_cd, data_src_m_cd, data_src_s_cd)
    cleanup_cycle: str = os.getenv("CLEAN_CYCLE", default="7")
