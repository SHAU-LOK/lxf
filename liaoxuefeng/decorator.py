from functools import wraps


def using_wrap(fn):
    @wraps
    def wrapper():
        print('enter ' + fn.__name__)
        fn()
        print('end ' + fn.__name__)
    return wrapper


def hello(fun):
    def wrapper():
        print(f'enter: {fun.__name__}')
        fun()
        print(f'end: {fun.__name__}')
    return wrapper


@hello
def foo():
    print('foo')


def makehtmlTag(tag, *args, **kwargs):
    def real_decorator(fn):
        css_class = " class='{}'".format(
            kwargs['css_class'] if 'css_class' in kwargs else '')

        def wrapped(*args, **kwargs):
            return "<" + tag + css_class + ">" + fn(*args, **kwargs) + "</" + tag + ">"

        return wrapped
    return real_decorator


@makehtmlTag(tag="b", css_class="bold_css")
@makehtmlTag(tag="c", css_class="italic_css")
def hello_html():
    return 'hello html'


if __name__ == '__main__':
    foo()

    print(hello_html())
    # >>><b class='bold_css'><c class='italic_css'>hello html</c></b>
