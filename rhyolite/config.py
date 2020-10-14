from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Mapping, Optional, Union


@dataclass
class Config:
    type_hooks: Mapping[Union[type, object], Callable[[Any], Any]] = field(default_factory=dict)
    cast: List[type] = field(default_factory=list)
    forward_references: Optional[Dict[str, Any]] = None
    check_types: bool = True
    strict: bool = False
    strict_unions_match: bool = False
