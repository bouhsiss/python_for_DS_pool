import sys
from ft_filter import ft_filter

def main():
    args = sys.argv[1:]

    assert len(args) == 2, "the arguments are bad"
    S = args[0]
    try :
        N = int(args[1])
    except ValueError:
        raise AssertionError("the arguments are bad")
    assert isinstance(S, str), "the arguments are bad"
    print (ft_filter(lambda x: len(x) > N, S.split()))



if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError: " + str(e))
