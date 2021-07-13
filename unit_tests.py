import shot

test_shot = shot.Shot(False, 'LEFT', 'LONG')


def test_success():
    assert test_shot.success is False


def test_line():
    assert test_shot.line == 'LEFT'


def test_relative_distance():
    assert test_shot.relative_distance == 'LONG'


test_success()
test_relative_distance()
test_line()
