try:
    from app.config.local_config import Config
except ImportError:
    from app.config.prd_config import Config

settings = Config()
