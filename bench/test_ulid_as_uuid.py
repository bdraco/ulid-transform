from uuid import UUID

import pytest

import ulid_transform
from bench.utils import suffix_benchmark_name


@pytest.mark.benchmark(group="ulid_as_uuid")
def test_ut_ulid_now_bytes(benchmark):
    suffix_benchmark_name(benchmark, ulid_transform.ulid_now_bytes)
    assert isinstance(
        benchmark(lambda: UUID(bytes=ulid_transform.ulid_now_bytes())),
        UUID,
    )


@pytest.mark.benchmark(group="ulid_as_uuid")
def test_ut_ulid_hex(benchmark):
    suffix_benchmark_name(benchmark, ulid_transform.ulid_hex)
    assert isinstance(benchmark(lambda: UUID(hex=ulid_transform.ulid_hex())), UUID)


@pytest.mark.benchmark(group="ulid_as_uuid")
def test_ulid2_uuid(benchmark):
    ulid2 = pytest.importorskip("ulid2")
    suffix_benchmark_name(benchmark, ulid2.generate_ulid_as_uuid)
    assert isinstance(benchmark(lambda: ulid2.generate_ulid_as_uuid()), UUID)


@pytest.mark.benchmark(group="ulid_as_uuid")
def test_ulidpy_uuid(benchmark):
    ulid = pytest.importorskip("ulid")
    suffix_benchmark_name(benchmark, ulid.new)
    assert isinstance(benchmark(lambda: ulid.new().uuid), UUID)
