from types import SimpleNamespace


def route(name, path, content):
    return SimpleNamespace(**dict(name=name, path=path, content=content))
