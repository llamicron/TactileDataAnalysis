import pytest

from docopt import docopt
from skippers import identify_skippers
from cli import __doc__ as doc
from cli import entry

class TestCli:
    def test_basic_skippers(self):
        args = docopt(doc, ['skippers', '5', '5'])
        cli_skippers = entry(args)

        skippers = identify_skippers(5, 5)
        assert cli_skippers == skippers

    def test_bad_values(self):
        args = docopt(doc, ['skippers', '0', '45'])
        with pytest.raises(ValueError):
            cli_skippers = entry(args)
        args = docopt(doc, ['skippers', '4', '67'])
        with pytest.raises(ValueError):
            cli_skippers = entry(args)

if __name__ == '__main__':
    pytest.main()
