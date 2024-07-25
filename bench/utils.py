from typing import Callable, Any


def get_func_impl_style(func: Callable[[Any], Any]) -> str:
    func_repr = repr(func)
    if func_repr.startswith("<cyfunction"):
        return "cython"
    if func_repr.startswith("<builtin"):
        return "builtin"
    return "py"


def suffix_benchmark_name(benchmark, func):
    style = get_func_impl_style(func)
    suffix = f"[{style}]"
    benchmark.name += suffix
    benchmark.fullname += suffix
    benchmark.extra_info["impl"] = style
