class BackendEngine(object):
    def write_request(self, request):
        raise NotImplemented

    def read_request(self, request):
        raise NotImplemented
