class ScheemsError(Exception):
    """
    The base Scheems Exception.

    All exceptions in the library inherits from this class.
    """


class UnsupportedTypeError(ScheemsError):
    """
    Exception raised when the SQLAlchemy type assigned
    to a column is not yet supported by Scheems.
    """


class MissingRequiredParameter(ScheemsError):
    """
    Exception raised when a required parameter was not
    passed with the request.
    """
