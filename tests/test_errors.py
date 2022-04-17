from opentraining.core.errors import OpenTrainingError, CompoundError


def test_compounderror():
    ce = CompoundError('top', errors=[OpenTrainingError('1', userdata=None), OpenTrainingError('2', userdata=None)], userdata=None)
    assert len(list(iter(ce))) == 3

    it = iter(ce)
    e = next(it)
    assert e.msg == 'top'

    e = next(it)
    assert e.msg == '1'

    e = next(it)
    assert e.msg == '2'

