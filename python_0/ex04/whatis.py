import sys

def even_or_odd(num):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main():
    try :
        args = sys.argv[1:]

        if len(args) == 0:
            exit()
        assert len(args) == 1, "one argument is required"

        try :
            number = int(args[0])
        except ValueError:
            raise AssertionError("argument is not a number")

        even_or_odd(number)
    except AssertionError as e:
        print("AssertionError: " + str(e))


if __name__ == "__main__":
    main()
    