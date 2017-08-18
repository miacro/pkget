import os


class Utils():
    def __init__(self):
        pass

    def set_value(target, name, value,
                  ignore_not_true=True, ignore_false=True,
                  ignore_none=True):
        if ignore_not_true and (not value):
            return value
        if ignore_none and value is None:
            return value
        elif ignore_false and value is False:
            return value

        if isinstance(target, list):
            target.append(value)
        elif isinstance(target, dict):
            target[name] = value
        else:
            setattr(target, name, value)
        return value

    def update_value(target, name, value, merge_value=True,
                     *args, **kwargs):
        def _set_value(target, name, value):
            return Utils.set_value(target, name, value, *args, **kwargs)

        if not merge_value:
            return _set_value(target, name, value)

        if isinstance(target, list):
            return _set_value(target, name, value)

        sub_target = None
        if isinstance(target, dict):
            sub_target = target[name]
        else:
            sub_target = getattr(target, name)

        if isinstance(sub_target, list) and isinstance(value, list):
            for i in range(len(value)):
                _set_value(sub_target, i, value[i])
        elif isinstance(sub_target, dict) and isinstance(value, dict):
            for i in value:
                _set_value(sub_target, i, value[i])
        else:
            _set_value(target, name, value)
        return value

    def abspath(path):
        if not path:
            return ""
        return os.path.abspath(
            os.path.expandvars(os.path.expanduser(path)))
