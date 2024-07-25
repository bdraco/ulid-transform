import pytest

import ulid_transform
from bench.utils import suffix_benchmark_name

example = "01J3MS6XG9XC7X9FR15J9A82ZP"


@pytest.mark.benchmark(group="ulid_parsing")
def test_ut_decode(benchmark):
    suffix_benchmark_name(benchmark, ulid_transform.ulid_to_bytes)
    assert isinstance(benchmark(lambda: ulid_transform.ulid_to_bytes(example)), bytes)


@pytest.mark.benchmark(group="ulid_parsing")
def test_ulid2_decode(benchmark):
    ulid2 = pytest.importorskip("ulid2")
    suffix_benchmark_name(benchmark, ulid2.decode_ulid_base32)
    assert isinstance(benchmark(lambda: ulid2.decode_ulid_base32(example)), bytes)


@pytest.mark.benchmark(group="ulid_parsing")
def test_ulidpy_decode(benchmark):
    ulid = pytest.importorskip("ulid")
    suffix_benchmark_name(benchmark, ulid.from_str)
    assert isinstance(benchmark(lambda: ulid.from_str(example).bytes), bytes)
