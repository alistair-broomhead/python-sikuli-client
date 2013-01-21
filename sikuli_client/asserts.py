"""
Repetitive asserts
"""


def assert_positive_int(pos_int, meth):
    """
    repetitive validation
    :param meth: calling method
    :param pos_int: int > 0
    """
    if not (isinstance(pos_int, int) and pos_int > 0):
        raise TypeError("%r expected positive integer, got %r" % (meth,
                                                                  pos_int))


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
    from .pattern import Pattern
    assert_one_of(PS, meth, [Pattern, basestring])
