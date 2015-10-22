import sys
import unittest


def main():
    tests_loader = unittest.TestLoader()
    tests = tests_loader.discover('.')
    runner = unittest.runner.TextTestRunner
    results = runner().run(tests)
    sys.exit(0 if results.errors else 1)


if __name__ == '__main__':
    main()
