import sys
from ft_filter import ft_filter


def main():
    try:
        args = sys.argv[1:]

        assert len(args) == 2, "the arguments are bad"
        S = args[0]
        assert isinstance(S, str), "the arguments are bad"
        try:
            N = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(ft_filter(lambda x: len(x) > N, S.split()))
    except AssertionError as e:
        print("AssertionError: " + str(e))


if __name__ == "__main__":
    main()
