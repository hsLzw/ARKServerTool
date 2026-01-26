import json
import os
import threading
from typing import Dict, Any, Optional

mods_config_path = "config/mods_settings/default.json"

class ModsSetting:

    _instance = None
    _initialized = False
    _write_lock = threading.Lock()

    def __new__(cls, config_path: str = mods_config_path):
        if cls._instance is None:
            cls._instance = super(ModsSetting, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path: str = mods_config_path):
        if not self._initialized:
            self.config_path = config_path
            self.config_data: Dict[str, Any] = {}
            self._load_config()
            self._initialized = True

    def _load_config(self) -> None:
        """加载或创建配置文件"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config_data = json.load(f)
            else:
                self.config_data = {}
                self._save_config()
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load config: {e}")

    def _save_config(self) -> None:
        """保存配置到文件"""
        with self._write_lock:
            try:
                with open(self.config_path, 'w+', encoding='utf-8') as f:
                    json.dump(self.config_data, f, indent=4, ensure_ascii=False)
            except IOError as e:
                raise RuntimeError(f"Failed to save config: {e}")

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """获取配置项"""
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """设置配置项"""
        self.config_data[key] = value
        self._save_config()

    def update(self, data: Dict[str, Any]) -> None:
        """批量更新配置"""
        self.config_data.update(data)
        self._save_config()

    def delete(self, key: str) -> None:
        """删除配置项"""
        if key in self.config_data:
            del self.config_data[key]
            self._save_config()

    def get_all(self) -> Dict[str, Any]:
        """获取全部配置"""
        return self.config_data.copy()

    def clear(self) -> None:
        """清空配置"""
        self.config_data.clear()
        self._save_config()

    def __contains__(self, key: str) -> bool:
        """支持 in 操作符检查"""
        return key in self.config_data

    def __getitem__(self, key: str) -> Any:
        """支持字典式访问"""
        return self.config_data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """支持字典式设置"""
        self.set(key, value)

    def __delitem__(self, key: str) -> None:
        """支持字典式删除"""
        self.delete(key)

    def __iter__(self):
        """支持 for k in config 的迭代操作"""
        return iter(self.config_data)

ins_mods_setting = ModsSetting()

