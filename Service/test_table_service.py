# from app import FlaskAppWrapper as app
import Controllers.app as app
from Actions.table_service_impl import TableServiceImpl

class TestTableService:
    def test_get_available_tables(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/1')
        assert response.status_code == 200
    
    def test_get_available_tables_incorrect_time_slot(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/13')
        assert response.status_code == 200

    def test_get_available_tables_incorrect_time_slot2(self):
        response = app.main().get_app().test_client().get('/tables/2022/10/13/0')
        assert response.status_code == 200

    def test_get_available_tables_incorrect_year(self):
        response = app.test_client().get('/tables/20224/10/13/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_month(self):
        response = app.test_client().get('/tables/2022/102/13/1')
        assert response.status_code == 400
    
    def test_get_available_tables_incorrect_day(self):
        response = app.test_client().get('/tables/2022/10/132/1')
        assert response.status_code == 400
    
    def test_get_available_tables_incorrect_date(self):
        response = app.test_client().get('/tables/2022/10/32/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_date2(self):
        response = app.test_client().get('/tables/2022/13/1/1')
        assert response.status_code == 400

    def test_get_available_tables_incorrect_date3(self):
        response = app.test_client().get('/tables/2022/0/1/1')
        assert response.status_code == 400

    def test_get_available_tables_invalid(self):
        response = app.test_client().get('/tables/aaaa/1/13/1')
        assert response.status_code == 404

    def test_get_available_tables_invalid2(self):
        response = app.test_client().get('/tables/2022/12//1')
        assert response.status_code == 404

    def test_post_reserved_tables_success(self):
        data = {
            "date": "2022-10-13",
            "time_slot_id": 1,
            "reservations": [4,5,6]
        }
        response = app.test_client().post('/tables', json=data)
        assert response.status_code == 200

    def test_post_reserved_tables_invalid_same_time_date_and_tables(self):
        data = {
            "date": "2022-10-13",
            "time_slot_id": 1,
            "reservations": [4,5,6]
        }
        response = app.test_client().post('/tables', json=data)
        assert response.status_code == 400

    def test_post_reserved_tables_invalid_same_time_date_and_tables2(self):
        data = {
            "date": "2022-10-13",
            "time_slot_id": 1,
            "reservations": [1,2,6]
        }
        response = app.test_client().post('/tables', json=data)
        assert response.status_code == 400

class TestTableServiceActions:
    def test_get_available_tables(self):
        response = TableServiceImpl.get_available_tables(2, '2019-12-02')
        assert response==  {
        "eight": 1,
        "eleven": 1,
        "five": 0,
        "four": 1,
        "nine": 1,
        "one": 0,
        "seven": 0,
        "six": 1,
        "ten": 0,
        "three": 0,
        "twelve": 1,
        "two": 0
    }
    
    def test_get_available_tables_incorrect_time_slot(self):
        response = TableServiceImpl.get_available_tables(13, '2019-12-02')
        assert response == {
        "eight": 1,
        "eleven": 1,
        "five": 1,
        "four": 1,
        "nine": 1,
        "one": 1,
        "seven": 1,
        "six": 1,
        "ten": 1,
        "three": 1,
        "twelve": 1,
        "two": 1
    }