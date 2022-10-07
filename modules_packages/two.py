#Two.py
import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
    print("TWO.PY is being ran directly!")
else:
    print('TWO.PY has been imported')
