import acp_times
import arrow

date = arrow.get(2021, 1, 1)


def test_start_times():
    assert acp_times.open_time(0, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T00:00'
    assert acp_times.close_time(0, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T01:00'


def test_open_edge_times():

    assert acp_times.open_time(200, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T05:53'
    assert acp_times.open_time(400, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T12:08'
    assert acp_times.open_time(600, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T18:48'
    assert acp_times.open_time(1000, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-02T09:05'

def test_open_times():
    print(date.format('YYYY-MM-DDTHH:mm'))
    print(acp_times.open_time(850, 200, date).format('YYYY-MM-DDTHH:mm'))
    assert acp_times.open_time(150, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T04:24'
    assert acp_times.open_time(350, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T10:34'
    assert acp_times.open_time(550, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T17:08'
    assert acp_times.open_time(850, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-02T03:43'

def test_close_edge_times():
    assert acp_times.close_time(200, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T13:20'
    assert acp_times.close_time(400, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-02T02:40'
    assert acp_times.close_time(600, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-02T16:00'
    assert acp_times.close_time(1000, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-04T03:00'


def test_close_times():
    assert acp_times.close_time(150, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T10:00'
    assert acp_times.close_time(350, 400, date).format('YYYY-MM-DDTHH:mm') == '2021-01-01T23:20'
    assert acp_times.close_time(550, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-02T12:40'
    assert acp_times.close_time(850, 200, date).format('YYYY-MM-DDTHH:mm') == '2021-01-03T13:52'

