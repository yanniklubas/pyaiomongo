import pathlib as pl
from dataclasses import dataclass
from typing import Any, Callable, Generic, Literal, Mapping, Sequence, Type

from bson.codec_options import TypeRegistry
from pymongo.driver_info import DriverInfo
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.server_api import ServerApi
from pymongo.server_description import ServerDescription

from pyaiomongo.core.types import DocumentType, Listeners


@dataclass
class InitKwargs(Generic[DocumentType, Listeners]):
    host: str | Sequence[str] | None
    port: int | None
    document_class: Type[DocumentType] 
    tz_aware: bool | None
    connect: bool | None
    type_registry: TypeRegistry | None
    direct_connection: bool | None
    max_pool_size: int | None
    min_pool_size: int
    max_idle_time_ms: int | None
    max_connecting: int
    timeout_ms: int | None
    connect_timeout_ms: int | None
    server_selector: Callable[[list[ServerDescription]], list[ServerDescription]] | None
    server_selection_timeout_ms: int
    wait_queue_timeout_ms: int | None
    heartbeat_frequency_ms: int
    app_name: str | None
    driver: DriverInfo | None
    event_listeners: Sequence[Listeners] | None
    retry_writes: bool
    retry_reads: bool
    compressors: set[Literal["snappy", "zlib", "zstd"]] | None
    z_lib_compression_level: Literal[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    uuid_representation: Literal["standard", "pythonLegacy", "javaLegacy", "csharpLegacy", "unspecified"]
    unicode_decode_error_handler: Literal["strict", "replace", "blackslashreplace", "surrogateescape", "ignore"]
    srv_service_name: str
    w: int | str | None
    w_timeout_ms: int | None
    journal: bool | None
    f_sync: bool | None
    replica_set: str | None
    read_preference: Literal["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest"]
    read_preference_tags: set[tuple[str, str]] | None
    max_staleness_seconds: int
    username: str | None
    password: str | None
    auth_source: str
    auth_mechanism: Literal["DEFAULT", "GSSAPI", "MONGODB-AWS", "MONGODB-X509", "PLAIN", "SCRAM-SHA-1", "SCRAM-SHA-256"]
    auth_mechanism_properties: str | None
    tls: bool
    tls_insecure: bool
    tls_allow_invalid_certificates: bool
    tls_allow_invalid_hostnames: bool
    tls_ca_file: pl.Path | None
    tls_certificate_key_file: pl.Path | None
    tls_crl_file: pl.Path | None
    tls_certificate_key_file_password: str | None
    tls_disable_ocsp_endpoint_check: bool
    ssl: bool
    read_concern_level: Literal["local", "available", "majority", "linearizable", "snapshot"] | None
    auto_encryption_ops: AutoEncryptionOpts | None
    server_api: ServerApi | None

class AsyncMongoClient(Generic[DocumentType]):
    HOST = "localhost"
    PORT = 27017

    _constructor_args = ("document_class", "tz_aware", "connect")

    def __init__(self,
                host: str | Sequence[str] | None = None,
                port: int | None = None,
                document_class: Type[DocumentType] | None = None,
                tz_aware: bool | None = None,
                connect: bool | None = None,
                type_registry: TypeRegistry | None = None,
                *,
                direct_connection: bool | None = None,
                max_pool_size: int | None = 50,
                min_pool_size: int = 0,
                max_idle_time_ms: int | None = None,
                max_connecting: int = 2,
                timeout_ms: int | None = None,
                connect_timeout_ms: int | None = 20000,
                server_selector: Callable[[list[ServerDescription]], list[ServerDescription]] | None = None,
                server_selection_timeout_ms: int = 30000,
                wait_queue_timeout_ms: int | None = None,
                heartbeat_frequency_ms: int = 10000,
                app_name: str | None = None,
                driver: DriverInfo | None = None,
                event_listeners: Sequence[Listeners] | None = None,
                retry_writes: bool = True,
                retry_reads: bool = True,
                compressors: set[Literal["snappy", "zlib", "zstd"]] | None = None,
                z_lib_compression_level: Literal[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = -1,
                uuid_representation: Literal["standard", "pythonLegacy", "javaLegacy", "csharpLegacy", "unspecified"] = "standard",
                unicode_decode_error_handler: Literal["strict", "replace", "blackslashreplace", "surrogateescape", "ignore"] = "strict",
                srv_service_name: str = "mongodb",
                w: int | str | None = None,
                w_timeout_ms: int | None = None,
                journal: bool | None = None,
                f_sync: bool | None = None,
                replica_set: str | None = None,
                read_preference: Literal["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest"] = "primary",
                read_preference_tags: set[tuple[str, str]] | None = None,
                max_staleness_seconds: int = -1,
                username: str | None = None,
                password: str | None = None,
                auth_source: str = "admin",
                auth_mechanism: Literal["DEFAULT", "GSSAPI", "MONGODB-AWS", "MONGODB-X509", "PLAIN", "SCRAM-SHA-1", "SCRAM-SHA-256"] = "SCRAM-SHA-1",
                auth_mechanism_properties: str | None = None,
                tls: bool = False,
                tls_insecure: bool = False,
                tls_allow_invalid_certificates: bool = False,
                tls_allow_invalid_hostnames: bool = False,
                tls_ca_file: pl.Path | None = None,
                tls_certificate_key_file: pl.Path | None = None,
                tls_crl_file: pl.Path | None = None,
                tls_certificate_key_file_password: str | None = None,
                tls_disable_ocsp_endpoint_check: bool = False,
                ssl: bool = False,
                read_concern_level: Literal["local", "available", "majority", "linearizable", "snapshot"] | None = None,
                auto_encryption_ops: AutoEncryptionOpts | None = None,
                server_api: ServerApi | None = None,
                ) -> None:
        self.__init_kwargs: InitKwargs[Mapping[str, Any], Listeners] = InitKwargs(
            host=host,
            port=port,
            document_class=document_class or dict[str, Any],
            tz_aware=tz_aware,
            connect=connect,
            type_registry=type_registry,
            direct_connection=direct_connection,
            max_pool_size=max_pool_size,
            min_pool_size=min_pool_size,
            max_idle_time_ms=max_idle_time_ms,
            max_connecting=max_connecting,
            timeout_ms=timeout_ms,
            connect_timeout_ms=connect_timeout_ms,
            server_selector=server_selector,
            server_selection_timeout_ms=server_selection_timeout_ms,
            wait_queue_timeout_ms=wait_queue_timeout_ms,
            heartbeat_frequency_ms=heartbeat_frequency_ms,
            app_name=app_name,
            driver=driver,
            event_listeners=event_listeners,
            retry_writes=retry_writes,
            retry_reads=retry_reads,
            compressors=compressors,
            z_lib_compression_level=z_lib_compression_level,
            uuid_representation=uuid_representation,
            unicode_decode_error_handler=unicode_decode_error_handler,
            srv_service_name=srv_service_name,
            w=w,
            w_timeout_ms=w_timeout_ms,
            journal=journal,
            f_sync=f_sync,
            replica_set=replica_set,
            read_preference=read_preference,
            read_preference_tags=read_preference_tags,
            max_staleness_seconds=max_staleness_seconds,
            username=username,
            password=password,
            auth_source=auth_source,
            auth_mechanism=auth_mechanism,
            auth_mechanism_properties=auth_mechanism_properties,
            tls=tls,
            tls_insecure=tls_insecure,
            tls_allow_invalid_certificates=tls_allow_invalid_certificates,
            tls_allow_invalid_hostnames=tls_allow_invalid_hostnames,
            tls_ca_file=tls_ca_file,
            tls_certificate_key_file=tls_certificate_key_file,
            tls_crl_file=tls_crl_file,
            tls_certificate_key_file_password=tls_certificate_key_file_password,
            tls_disable_ocsp_endpoint_check=tls_disable_ocsp_endpoint_check,
            ssl=ssl,
            read_concern_level=read_concern_level,
            auto_encryption_ops=auto_encryption_ops,
            server_api=server_api
        )



