"""
Repetitive asserts
"""


def assert_int(int_, meth):
    """
    repetitive validation

    :param meth: calling method
    :param int_: int
    """
    if not isinstance(int_, int):
        raise TypeError("%r expected integer, got %r" % (meth, int_))


def assert_positive_int(pos_int, meth):
    """
    repetitive validation

    :param meth: calling method
    :param pos_int: int > 0
    """
    if not (isinstance(pos_int, int) and pos_int > 0):
        raise TypeError("%r expected positive integer, got %r" % (meth,
                                                                  pos_int))


def assert_positive_ints(pos_ints, meth, names=None):
    """
    repetitive validation

    :param meth: calling method
    :param pos_ints: iterable of int > 0
    :param names: iterable names of args (optional)
    """
    if names is None:
        iterable = ((str(x), y) for (x, y) in enumerate(pos_ints))
    elif len(names) >= len(pos_ints):
        iterable = zip(names, pos_ints)
    else:
        e_names = dict(enumerate(names))
        iterable = ((str(i) if i not in e_names else e_names[i], p)
                    for i, p in enumerate(pos_ints))
    for n, pos_int in iterable:
        if not (isinstance(pos_int, int) and pos_int > 0):
            raise TypeError("%r's argument '%s' expected positive integer"
                            ", got %r" % (meth, n, pos_int))


def assert_positive_num(pos_num, meth):
    """
    repetitive validation

    :param meth: calling method
    :param pos_num: number > 0
    """
    if not pos_num > 0 or not (isinstance(pos_num, int) or
                               isinstance(pos_num, float)):
        raise TypeError("%r expected positive integer, got %r" % (meth,
                                                                  pos_num))

def assert_one_of(test, meth, types):
    """
    repetitive validation

    :param meth: calling method
    :param test: one of types
    :param types: list of types
    """
    for t_ in types:
        if isinstance(test, t_):
            return
    raise TypeError("%r expected one of %r, got %r" % (meth, types, test))


def assert_PS(PS, meth):
    """
    repetitive validation

    :param meth: calling method
    :param PS: Pattern or str
    """
    from python_sikuli_client.pattern import Pattern

    assert_one_of(PS, meth, [Pattern, basestring])


def assert_PSMRL(PSMRL, meth):
    """
    repetitive validation

    :param meth: calling method
    :param PSMRL: Pattern, str, Match, Region or Location
    """
    from python_sikuli_client.classes import Pattern, Match, Region, Location

    assert_one_of(PSMRL, meth, [Pattern, basestring, Match, Region, Location])


def assert_PSML(PSMRL, meth):
    """
    repetitive validation

    :param meth: calling method
    :param PSMRL: Pattern, str, Match or Location
    """
    from python_sikuli_client.classes import Pattern, Match, Location

    assert_one_of(PSMRL, meth, [Pattern, basestring, Match, Location])


def assert_PSRM(PSRM, meth):
    """
    repetitive validation

    :param meth: calling method
    :param PSRM: Pattern, str, Region or Match
    """
    from python_sikuli_client.classes import Pattern, Match, Region

    assert_one_of(PSRM, meth, [Pattern, basestring, Region, Match])


def assert_Region(region, meth):
    """
    repetitive validation

    :param meth: calling method
    :param region: Region
    """
    from python_sikuli_client.classes import Region
    if not isinstance(region, Region):
        raise TypeError("%r expected Region, got %r" % (meth, region))
