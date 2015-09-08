# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

class const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const. %s" % name
        if not name.isupper():
            raise self.ConstCaseError, \
                    'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value


if __name__ == '__main__':
    class Const_specific(const):
        pass
    Const_specific.AB = 5
    print Const_specific.AB