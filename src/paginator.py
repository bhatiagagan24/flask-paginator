
class Paginator:
    
    def __init__(self, page_size : int):
        if page_size < 0:
            self.page_size = 0
        else:
            self.page_size = page_size

    def fetch_page_size(self):
        return self.page_size
    