# caller.py
import receiver

print("caller_haha")
print(__name__)

def test():
    print("caller_test can be called!")


def caller_print():
    print("I'm caller.py")


if __name__ == '__main__':
    caller_print()
    test()