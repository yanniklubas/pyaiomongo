from typing import Any, Mapping, Optional, TypeVar

from pymongo.monitoring import \
    _EventListener  # pyright: ignore [reportPrivateUsage]

DocumentType = TypeVar("DocumentType", bound=Mapping[str, Any])


Listeners = TypeVar("Listeners", bound=_EventListener)

Address = tuple[str, Optional[int]]