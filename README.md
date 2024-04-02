# YouTube Crawler

## envs

| Name           | Description   | Example                                     | Default                     |
|----------------|---------------|---------------------------------------------|-----------------------------|
| TARGET_URL     | 크롤링 타겟 url    | https://www.youtube.com/watch?v=6QZ_qc75ihU |                             |
| TMP_DIR        | 임시 저장 경로      | /data/nas/yt_crawling/tmp                   |                             |
| SAVE_DIR       | 결과 저장 경로      | /data/nas/yt_crawling/output                |                             |
| FILENAME       | 저장파일 이름       | 연합뉴스(%Y.%m.%d %H-%M-00)                     | streaming-%Y-%m-%d_%H_%M_%S |
| STREAM_QUALITY | 스트리밍 품질       | 360p / 720p / 1080p                         | 1080p                       |
| CRAWLING_TYPE  | 크롤링 타입        | video / audio                               |                             |
| SPLIT_TIME     | 분할 시간(초)      | 300                                         |                             |
| DATA_SRC_L_CD  | 데이터 출처 대분류 코드 | C001                                        |                             |
| DATA_SRC_M_CD  | 데이터 출처 중분류 코드 | 202                                         |                             |
| DATA_SRC_S_CD  | 데이터 출처 소분류 코드 | 3401                                        |                             |
| CLEANUP_CYCLE  | 삭제 주기(일)      | 7                                           | 7                           |
