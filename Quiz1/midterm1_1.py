class TreeOrders:
    def read(self):
        self.n = int(input())
        self.keys = []
        self.left = []
        self.right = []
        for _ in range(self.n):
            key, left, right = map(int, input().split())
            self.keys.append(key)
            self.left.append(left)
            self.right.append(right)

    def in_order(self, index):
        if index == -1:
            return
        self.in_order(self.left[index])
        self.result_in_order.append(self.keys[index])
        self.in_order(self.right[index])

    def pre_order(self, index):
        if index == -1:
            return
        self.result_pre_order.append(self.keys[index])
        self.pre_order(self.left[index])
        self.pre_order(self.right[index])

    def post_order(self, index):
        if index == -1:
            return
        self.post_order(self.left[index])
        self.post_order(self.right[index])
        self.result_post_order.append(self.keys[index])

    def solve(self):
        self.result_in_order = []
        self.result_pre_order = []
        self.result_post_order = []
        self.in_order(0)
        self.pre_order(0)
        self.post_order(0)
        print(" ".join(map(str, self.result_in_order)))
        print(" ".join(map(str, self.result_pre_order)))
        print(" ".join(map(str, self.result_post_order)))

tree = TreeOrders()
tree.read()
tree.solve()
