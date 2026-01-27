import json
import os
import threading
from typing import Dict, Any, Optional, TypeVar, Type

T = TypeVar('T', bound='BaseJsonSettings')


class BaseJsonSettings:
    """Base class for JSON-based configuration management"""

    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config_data: Dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """Load or create configuration file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config_data = json.load(f)
            else:
                os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
                self.config_data = {}
                self._save_config()
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load config: {e}")

    def _save_config(self) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w+', encoding='utf-8') as f:
                json.dump(self.config_data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise RuntimeError(f"Failed to save config: {e}")

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get configuration item"""
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration item"""
        self.config_data[key] = value
        self._save_config()

    def update(self, data: Dict[str, Any]) -> None:
        """Batch update configuration"""
        self.config_data.update(data)
        self._save_config()

    def delete(self, key: str) -> None:
        """Delete configuration item"""
        if key in self.config_data:
            del self.config_data[key]
            self._save_config()

    def get_all(self) -> Dict[str, Any]:
        """Get all configurations"""
        return self.config_data.copy()

    def clear(self) -> None:
        """Clear all configurations"""
        self.config_data.clear()
        self._save_config()

    def __contains__(self, key: str) -> bool:
        """Support 'in' operator"""
        return key in self.config_data

    def __getitem__(self, key: str) -> Any:
        """Support dictionary-style access"""
        return self.config_data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """Support dictionary-style setting"""
        self.set(key, value)

    def __delitem__(self, key: str) -> None:
        """Support dictionary-style deletion"""
        self.delete(key)

    def __iter__(self):
        """Support iteration"""
        return iter(self.config_data)


class ModsSetting(BaseJsonSettings):
    """Singleton implementation for mods settings"""

    _instance = None
    _write_lock = threading.Lock()
    _initialized = False

    def __new__(cls, config_path: str = "config/mods_settings/default.json"):
        if cls._instance is None:
            cls._instance = super(ModsSetting, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path: str = "config/mods_settings/default.json"):
        if not self._initialized:
            super().__init__(config_path)
            self._initialized = True

    def _save_config(self) -> None:
        """Thread-safe save with class-specific lock"""
        with self._write_lock:
            super()._save_config()

class WorldInfo(BaseJsonSettings):
    """Singleton implementation for mods settings"""

    _instance = None
    _write_lock = threading.Lock()
    _initialized = False

    def __new__(cls, config_path: str = "config/run_settings/world_info.json"):
        if cls._instance is None:
            cls._instance = super(WorldInfo, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path: str = "config/run_settings/world_info.json"):
        if not self._initialized:
            super().__init__(config_path)
            self._initialized = True

    def _save_config(self) -> None:
        """Thread-safe save with class-specific lock"""
        with self._write_lock:
            super()._save_config()

ins_mods_setting = ModsSetting()
ins_world_info = WorldInfo()
