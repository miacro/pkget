from pkget import PkgetError


def set_value(target, name, value,
              ignore_empty=True, ignore_false=True,
              ignore_none=True):
    if ignore_none and value is None:
        return value
    if ignore_false and value is False:
        return value
    if ignore_empty and (not value):
        return value

    if isinstance(target, list):
        target.append(value)
    elif isinstance(target, dict):
        target[name] = value
    else:
        setattr(target, name, value)
    return value


def update_value(target, name, value, merge_value=True,
                 ignore_empty=True, ignore_false=True,
                 ignore_none=True):
    def _set_value(target, name, value):
        return set_value(
            target, name, value, ignore_empty=ignore_empty,
            ignore_false=ignore_false, ignore_none=ignore_none)

    if not merge_value:
        return _set_value(target, name, value)

    if isinstance(target, list):
        return _set_value(target, name, value)

    def _get_subobject(target, name):
        if isinstance(target, dict):
            return target[name]
        else:
            return getattr(target, name)

    if isinstance(_get_subobject(target, name), list):
        if not isinstance(value, list):
            raise PkgetError("value of %s is not list" % name,
                             "value")
        for i in range(len(value)):
            _set_value(_get_subobject(target, name), i, value[i])
    elif isinstance(_get_subobject(target, name), dict):
        if not isinstance(value, dict):
            raise PkgetError("value of %s is not dict" % name,
                             "value")
        for i in value:
            _set_value(_get_subobject(target, name), i, value[i])
    else:
        _set_value(target, name, value)
    return value
