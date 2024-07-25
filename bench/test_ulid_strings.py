import pytest

import ulid_transform
from bench.utils import suffix_benchmark_name


@pytest.mark.benchmark(group="ulid_strings")
def test_ut_ulid_now(benchmark):
    suffix_benchmark_name(benchmark, ulid_transform.ulid_now)
    assert isinstance(benchmark(lambda: ulid_transform.ulid_now()), str)


@pytest.mark.benchmark(group="ulid_strings")
def test_ut_ulid_at_time(benchmark):
    suffix_benchmark_name(benchmark, ulid_transform.ulid_at_time)
    assert isinstance(benchmark(lambda: ulid_transform.ulid_at_time(1)), str)


@pytest.mark.benchmark(group="ulid_strings")
def test_ulid2_ulid_now(benchmark):
    ulid2 = pytest.importorskip("ulid2")
    suffix_benchmark_name(benchmark, ulid2.generate_ulid_as_base32)
    assert isinstance(benchmark(lambda: ulid2.generate_ulid_as_base32()), str)


@pytest.mark.benchmark(group="ulid_strings")
def test_ulid2_ulid_at_time(benchmark):
    ulid2 = pytest.importorskip("ulid2")
    suffix_benchmark_name(benchmark, ulid2.generate_ulid_as_base32)
    assert isinstance(
        benchmark(lambda: ulid2.generate_ulid_as_base32(timestamp=1)), str
    )


@pytest.mark.benchmark(group="ulid_strings")
def test_ulidpy_uuid_now(benchmark):
    ulid = pytest.importorskip("ulid")
    suffix_benchmark_name(benchmark, ulid.new)
    assert isinstance(benchmark(lambda: ulid.new().str), str)


@pytest.mark.benchmark(group="ulid_strings")
def test_ulidpy_uuid_at_time(benchmark):
    ulid = pytest.importorskip("ulid")
    suffix_benchmark_name(benchmark, ulid.from_timestamp)
    assert isinstance(benchmark(lambda: ulid.from_timestamp(timestamp=1).str), str)
