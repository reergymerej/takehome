from typing import List, Tuple

def get_source(args: List[str]) -> str:
    try:
        return args[0]
    except IndexError:
        return "./inputs"

def get_dest(args: List[str]) -> str:
    try:
        return args[1]
    except IndexError:
        return "./output"

def get_paths(args: List[str]) -> Tuple[str, str]:
    return (
        get_source(args),
        get_dest(args)
    )