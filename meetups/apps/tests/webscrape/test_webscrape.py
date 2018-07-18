from mock import patch

from apps.webscrape import content_to_csv, get_content


target = 'apps.webscrape.get_content'


class TestWebscrape(object):
    def test_get_content(self):
        data = get_content()

        assert len(data) > 0

    def test_mock_get_content(self, capsys):
        with patch(target) as mock_wscrape:
            mock_wscrape.return_value = [
                'https://godjango.com',
                'https://www.anaconda.com',
                'http://www.blog.pythonlibrary.org'
            ]
            content_to_csv()

            assert mock_wscrape.call_count == 1

            out, err = capsys.readouterr()

            assert out == (
                'Link\r\n'
                'https://godjango.com\r\n'
                'https://www.anaconda.com\r\n'
                'http://www.blog.pythonlibrary.org\r\n\r\n'
            )
