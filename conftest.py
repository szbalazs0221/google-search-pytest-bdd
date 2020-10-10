"""Project level fixtures, hooks and custom command line arguments"""

from time import strftime


def pytest_addoption(parser):
    """Custom command line options.

    :param parser: Parser for command line arguments and ini-file values.
    :type parser: Parser
    """
    parser.addoption(
        "--webdriver",
        action='store',
        choices=['Chrome', 'Firefox', 'Ie', 'Safari', 'Edge'],
        required=True)


def pytest_bdd_step_error(step_func_args):
    """Pytest-bdd hook which will execute if any error occur in a step.
    This will create a screenshot of the actual browser page.

    :param step_func_args: All step funtion arguments
    :type step_func_args: dict
    """
    path = f'reports/screenshots/screenshot_{strftime("%H_%M")}.png'
    step_func_args['webdriver'].save_screenshot(path)
