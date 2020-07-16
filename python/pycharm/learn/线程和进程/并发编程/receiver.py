# receiver.py
print("receiver_haha")
print(__name__)

def test():
    print("test can be called!")


def receiver_print():
    print("I'm receiver.py")


if __name__ == '__main__':
    receiver_print()