class RceException(Exception):
    """Base Yun Exception."""
    default_msg = 'An unknown exception occured.'
    code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if not message:
            try:
                message = self.default_msg.format(**self.kwargs)
            except Exception:
                message = self.default_msg

        self.message = message
        super(RceException, self).__init__(self.message)
