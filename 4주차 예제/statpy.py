class discstat:
    def get_avg(self):
        return ("avg")
    def get_dev(self):
        return "dev"

class teststat:
    name="Test Statistics"
    def t_test(self):
        return "t-test"
    def get_name(self):
        return self.name
if __name__ == "__main__":
    ta=teststat()
    print(ta.name)
    print(ta.get_name())
    ds=discstat()
    print(ds.get_avg())