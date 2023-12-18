import logging


class CustomFormatter(logging.Formatter):
    """
    Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629.
    ANSI colors: https://talyian.github.io/ansicolors/.
    """

    TURQUOISE = "\x1b[38;5;43m"  # DEBUG
    BLUE = "\x1b[38;5;39m"  # INFO
    ORANGE = "\x1b[38;5;214m"  # WARNING
    BOLD_RED = "\x1b[31;1m"  # ERROR  |  EXCEPTION
    RED = "\x1b[38;5;196m"  # CRITICAL
    RESET = "\x1b[0m"  # Close of ANSI colors code

    def __init__(self, fmt) -> None:
        """Setting custom colors for the `format()` function.

        FORMATS = {
            10: TURQUOISE color,  -> DEBUG
            20: BLUE color,       -> INFO
            30: ORANGE color,     -> WARNING
            40: BOLD RED color,   -> ERROR  |  EXCEPTION
            50: RED color         -> CRITICAL
        }"""

        super().__init__()

        self._fmt: str = fmt
        self.FORMATS: {int: str} = {
            logging.DEBUG: self.TURQUOISE + self._fmt + self.RESET,
            logging.INFO: self.BLUE + self._fmt + self.RESET,
            logging.WARNING: self.ORANGE + self._fmt + self.RESET,
            logging.ERROR: self.BOLD_RED + self._fmt + self.RESET,
            logging.CRITICAL: self.RED + self._fmt + self.RESET,
        }

    def format(self, record) -> str:
        """The logging level is obtained from the record parameter, and the corresponding color is set."""

        formatter: logging.Formatter = logging.Formatter(fmt=self.FORMATS.get(record.levelno))

        return formatter.format(record=record)
