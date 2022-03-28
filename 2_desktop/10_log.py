import logging
from datetime import datetime
# 기본값
# level=logging.DEBUG : 레벨이 디버그 이상 보여줌
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")


# # 로그 레벨 크기 : debug < info < warning < error < critical
# logging.debug("???")
# logging.info("자동화 수행 준비")
# logging.warning("슼크랩트가 오래 되었습니다, 실행상 문제가 있을 수 있습니다.")
# logging.error("에로 발생, 에러코드 ..")
# logging.critical("복구 불가능한 심각한 문제 발생")

# 터미널과 파일에 로그 남기기
# 시간 [로그레벨] 메시지 형태로 로그를 작성
logformatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림(터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logformatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logformatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행")
