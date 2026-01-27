import threading
from typing import List, Dict, Tuple, Optional
from datetime import datetime


class TooleLogger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._init_logger()
        return cls._instance

    def _init_logger(self):
        """Initialize logger"""
        self._logs: List[Dict[str, str]] = []
        self._max_logs = 100
        self._log_lock = threading.Lock()

    def add_log(self, content: str, log_type: str = "info") -> None:
        """
        添加日志
        :param content: 日志内容
        :param log_type: 日志类型 (info/warning/error等)
        """
        with self._log_lock:
            # 创建日志条目
            log_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": log_type.lower(),
                "content": content
            }

            # 添加日志
            self._logs.append(log_entry)

            # 限制日志数量
            if len(self._logs) > self._max_logs:
                self._logs.pop(0)

    def get_all_logs(self) -> List[Dict[str, str]]:
        """
        获取全部日志
        :return: 日志列表，按时间从旧到新排序
        """
        with self._log_lock:
            return self._logs.copy()

    def clear_logs(self) -> None:
        """清空日志"""
        with self._log_lock:
            self._logs.clear()

ins_tool_logger = TooleLogger()
