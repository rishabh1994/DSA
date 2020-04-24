class RouteTrie:
    def __init__(self, handler):
        self.rootNode = RouteTrieNode(handler)

    def insert(self, path, handlerName):
        self.rootNode.insert(path, self.rootNode, handlerName)

    def find(self, path):
        pointer = self.rootNode
        split = path.split("/")
        for singlePath in split:
            if singlePath not in pointer.children.keys():
                return None
            pointer = pointer.children[singlePath]
        return pointer.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, path, rootNode, handlerName):
        pointer = rootNode
        if path:
            split = path.split("/")
            for singlePath in split:
                if singlePath not in pointer.children.keys():
                    pointer.children[singlePath] = RouteTrieNode()
                pointer = pointer.children[singlePath]

            pointer.handler = handlerName


class Router:
    def __init__(self, homePageHandler, notFoundHandler):
        self.router = RouteTrie(homePageHandler)
        self.notFoundHandler = RouteTrie(notFoundHandler)

    def add_handler(self, path, handlerName):
        self.router.insert(path, handlerName)

    def lookup(self, path):
        if path:
            if path == "/" or path == "//":
                return self.router.rootNode.handler
            if self.router.find(path):
                return self.router.find(path)
            else:
                if path[-1] == "/":
                    path = path[:-1]
                    if self.router.find(path):
                        return self.router.find(path)
        return self.notFoundHandler.rootNode.handler


def first_test_case():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler'
    print(router.lookup("/home/about/me"))  # should print 'not found handler'


def second_test_case():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup(None))  # should print 'not found handler' as we are looking up for None.
    print(router.lookup(""))  # should print 'not found handler' as we are looking up for Empty String.


def third_test_case():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler'
    print(router.lookup("/home/about//"))  # should print 'not found handler' as only 1 trailing / is allowed.


def fourth_test_case():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/login", "about login")
    router.add_handler("/home/login/newUser", "about login for new User")
    router.add_handler("/home/login/oldUser", "about login for old User")
    router.add_handler("/home/articles", "about articles")

    print(router.lookup("/home/login"))  # should print 'about login'
    print(router.lookup("/home/login/"))  # should print 'about login'
    print(router.lookup("/home/login/newUser"))  # should print 'about login for new User'
    print(router.lookup("/home/login/newUser/"))  # should print 'about login for new User'
    print(router.lookup("/home/login/oldUser"))  # should print 'about login for old User'
    print(router.lookup("/home/login/oldUser/"))  # should print 'about login for old User'
    print(router.lookup("/home/articles"))  # should print 'about articles'
    print(router.lookup("/home/articles/"))  # should print 'about articles'


first_test_case()
second_test_case()
third_test_case()
fourth_test_case()
