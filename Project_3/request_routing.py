class RouteTrieNode(object):
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_block):
        if path_block not in self.children:
            self.children[path_block] = RouteTrieNode()


class RouteTrie(object):
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        node = self.root

        for path_block in path:
            node.insert(path_block)
            node = node.children[path_block]

        node.handler = handler

    def find(self, path):
        node = self.root

        for path_block in path:
            if path_block not in node.children:
                return None
            node = node.children[path_block]

        return node.handler


class Router:
    def __init__(self, root_handler, non_found_handler):
        self.router = RouteTrie(root_handler=root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, raw_path, handler):
        path = self._split_path(raw_path)
        self.router.insert(path=path, handler=handler)

    def lookup(self, raw_path):
        path = self._split_path(raw_path)

        if len(path) == 0:
            return self.router.handler

        finding = self.router.find(path=path)

        if finding is None:
            return self.non_found_handler
        else:
            return finding

    @staticmethod
    def _split_path(raw_path):
        result_temp = raw_path.split(sep="/")
        return [element for element in result_temp if element != ""]


def main():
    # Here are some test cases and expected outputs you can use
    # to test your implementation
    # create the router and add a route
    # remove the 'not found handler' if you did not implement this
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home"))
    print(router.lookup("/home/about"))  # should print 'about handler'
    # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/"))
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about/me"))


if __name__ == "__main__":
    main()
