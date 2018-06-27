from apps.webscrape import get_content


class TestWebscrape(object):
    def test_get_content(self):
        data = get_content()

        assert len(data) > 0
