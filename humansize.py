SUFFIXES = {
     1000: ['KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB'],
     1024: ['KiB', 'MiB', 'GiB', 'TiB', 'EiB', 'ZiB', 'YiB']
    }

def humanize(size, use_1024=True):
    '''
    Convert a file size to human readable form.

    Parameters:
    size => file size in bytes
    use_1024 => True/False, use multiples of 1024 or 1000

    Returns: string
    '''

    if size < 0:
        raise ValueError('Negativity will not be tolerated')

    multiple = 1024 if use_1024 else 1000
    temp = size
    i = 0

    while (temp >= multiple):
        temp /= multiple
        i += 1
        if i > len(SUFFIXES[multiple]):
            raise ValueError("Wow that's too big")

    # print(f"{size} can be read as {temp}{SUFFIXES[multiple][i-1]}")
    return '{0:.1f} {1}'.format(temp, SUFFIXES[multiple][i-1])
