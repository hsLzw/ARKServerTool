import configparser
import os
import threading
from typing import Dict, Any, Optional

class BaseSetting:
    _instance = None
    _initialized = False
    _write_lock = threading.Lock()

    def __new__(cls, config_path: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_path: str):
        if not self._initialized:
            self.config_path = config_path
            self.config = configparser.ConfigParser()
            self._load_config()
            self._initialized = True

    def _load_config(self) -> None:
        """加载或创建配置文件"""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config.read_file(f)
            else:
                self._save_config()
        except (configparser.Error, IOError) as e:
            raise RuntimeError(f"Failed to load config: {e}")

    def _save_config(self) -> None:
        """保存配置到文件"""
        with self._write_lock:
            try:
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    self.config.write(f)
            except IOError as e:
                raise RuntimeError(f"Failed to save config: {e}")

    def get(self, section: str, key: str, default: Optional[Any] = "") -> Any:
        """获取配置项"""
        try:
            data = self.config.get(section, key)
            if data in ("True", "False", "true", "false"):
                return True if data in ("True", "true") else False
            return data
        except:
            return default

    def set(self, section: str, key: str, value: Any) -> None:
        """设置配置项"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))

    def update_section(self, section: str, data: Dict[str, Any]) -> None:
        """批量更新配置节"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        for key, value in data.items():
            self.config.set(section, key, str(value))
        self._save_config()

    def delete(self, section: str, key: str) -> None:
        """删除配置项"""
        try:
            self.config.remove_option(section, key)
            self._save_config()
        except configparser.NoSectionError:
            pass

    def delete_section(self, section: str) -> None:
        """删除整个配置节"""
        self.config.remove_section(section)
        self._save_config()

    def get_section(self, section: str) -> Dict[str, str]:
        """获取整个配置节"""
        if self.config.has_section(section):
            return dict(self.config.items(section))
        return {}

    def clear(self) -> None:
        """清空配置"""
        for section in self.config.sections():
            self.config.remove_section(section)
        self._save_config()

    def __contains__(self, section_key: str) -> bool:
        """支持 in 操作符检查节是否存在"""
        section, _, key = section_key.partition('.')
        if key:
            return self.config.has_option(section, key)
        return self.config.has_section(section)

    def __getitem__(self, section_key: str) -> Any:
        """支持字典式访问 section.key"""
        section, _, key = section_key.partition('.')
        if not key:
            raise KeyError("Must specify section and key like 'section.key'")
        return self.get(section, key)

    def __setitem__(self, section_key: str, value: Any) -> None:
        """支持字典式设置 section.key"""
        section, _, key = section_key.partition('.')
        if not key:
            raise KeyError("Must specify section and key like 'section.key'")
        self.set(section, key, value)

    def __delitem__(self, section_key: str) -> None:
        """支持字典式删除 section.key"""
        section, _, key = section_key.partition('.')
        if not key:
            self.delete_section(section)
        else:
            self.delete(section, key)


class ServerSetting(BaseSetting):
    _instance = None
    _initialized = False

    def __new__(cls, config_path: str = "config/run_settings/default.ini"):
        if cls._instance is None:
            cls._instance = super().__new__(cls, config_path)
        return cls._instance

    def __init__(self, config_path: str = "config/run_settings/default.ini"):
        super().__init__(config_path)
        self.__server_info_key = "server_info"

    def save(self):
        self._save_config()

    def set_root_path(self, root_path: str) -> None:
        self.set(self.__server_info_key, "root_path", root_path)

    def set_server_pwd(self, server_pwd: str) -> None:
        self.set(self.__server_info_key, "server_pwd", server_pwd)

    def set_admin_pwd(self, admin_pwd: str) -> None:
        self.set(self.__server_info_key, "admin_pwd", admin_pwd)

    def set_max_player(self, max_player: int) -> None:
        self.set(self.__server_info_key, "max_player", max_player)

    def set_cluster_id(self, cluster_id: str) -> None:
        self.set(self.__server_info_key, "cluster_id", cluster_id)

    def set_cluster_path(self, cluster_path: str) -> None:
        self.set(self.__server_info_key, "cluster_path", cluster_path)

    def set_be_open(self, is_open: bool) -> None:
        self.set(self.__server_info_key, "be_open", is_open)

    def set_mods_open(self, is_open: bool) -> None:
        self.set(self.__server_info_key, "mods_open", is_open)

    def set_more_worlds_open(self, is_open: bool) -> None:
        self.set(self.__server_info_key, "more_worlds_open", is_open)

    def set_server_session_name(self, name) -> None:
        self.set(self.__server_info_key, "server_session_name", name)

    @property
    def root_path(self) -> str:
        return self.get(self.__server_info_key, "root_path")

    @property
    def server_pwd(self) -> str:
        return self.get(self.__server_info_key, "server_pwd")

    @property
    def admin_pwd(self) -> str:
        return self.get(self.__server_info_key, "admin_pwd")

    @property
    def max_player(self) -> int:
        return int(self.get(self.__server_info_key, "max_player", 30))

    @property
    def cluster_id(self) -> str:
        return self.get(self.__server_info_key, "cluster_id")

    @property
    def cluster_path(self) -> str:
        return self.get(self.__server_info_key, "cluster_path")

    @property
    def be_open(self) -> bool:
        return self.get(self.__server_info_key, "be_open", False)

    @property
    def mods_open(self) -> bool:
        return self.get(self.__server_info_key, "mods_open", False)

    @property
    def more_worlds_open(self) -> bool:
        return self.get(self.__server_info_key, "more_worlds_open", False)

    @property
    def server_session_name(self) -> str:
        return self.get(self.__server_info_key, "server_session_name", "")


class GameSetting(BaseSetting):
    _instance = None
    _initialized = False
    _current_config_path = "config/game_settings/default.ini"  # 默认路径

    def __new__(cls, config_path: str = None):
        if cls._instance is None:
            if config_path:
                cls._current_config_path = config_path
            cls._instance = super().__new__(cls, cls._current_config_path)
        return cls._instance

    def __init__(self, config_path: str = None):
        if config_path:
            self.change_config_path(config_path)
        super().__init__(self._current_config_path)

    @classmethod
    def change_config_path(cls, new_path: str) -> None:
        """动态更改配置文件路径"""
        if not new_path.endswith('.ini'):
            new_path = f"config/game_settings/{new_path}.ini"
        cls._current_config_path = new_path

        if cls._instance:
            # 关键修改：重新创建 ConfigParser 实例并加载新文件
            cls._instance.config = configparser.ConfigParser()
            cls._instance.config_path = new_path
            cls._instance._load_config()

# 创建单例实例
ins_server_setting = ServerSetting()
ins_game_setting = GameSetting()
