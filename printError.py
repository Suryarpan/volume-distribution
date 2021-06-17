from os import abort


def printErr(err, level=0):
    level_str = ''
    if level == 1:
        level_str = 'NOTE: '
    elif level == 2:
        level_str = 'WARN: '
    elif level > 2:
        level_str = 'FATAL: '

    print(f'VolDist: {level_str}{err.strerror}')
    if level > 2:
        abort()
