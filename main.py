import hashlib
from typing import Union, Dict, Any

class calc:
    def __init__(self) -> None:
        """
        calculate file hash.
        """
        self._current_file: str = None
        self._hash_type: str = None
        self._map_hash: Dict[str, Any] = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256,
            "sha512": hashlib.sha512
        }
    
    def __call__(self, *args, **kwargs) -> None:
        """
        just debug
        """
        return f"<calc hash:({self._current_file}, {self._map_hash[self._hash_type]()})>"
    
    @property
    def current_process(self) -> Union[str, None]:
        """
        current process file
        """
        return self._current_file
    
    def hashfile(self, file_path: str, hash_type: str = 'sha256') -> Union[str, bytes]:
        """
        hashfile, can be check with this.
        """
        from pathlib import Path
        self._hash_type: str = hash_type
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError("file are not found")
        
        if self._hash_type and self._hash_type not in self._map_hash.keys():
            raise TypeError("hash type not identified in our map hash.")
        
        hash_func = self._map_hash[self._hash_type]()
        with open(file.absolute(), "rb") as fp:
            while chunk := fp.read(4096):
                hash_func.update(chunk)
                
        return hash_func.hexdigest()
    
    