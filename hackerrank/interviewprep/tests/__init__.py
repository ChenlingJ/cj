from textwrap import dedent


def patch_io(module: object, input: str) -> list[str]:
    input_iter = iter(dedent(input).strip().splitlines())
    module.input = lambda *_: next(input_iter)
    print_list = []

    def patched_print(*args, sep=" "):
        print_list.append(sep.join(map(str, args)))

    module.print = patched_print

    return print_list
