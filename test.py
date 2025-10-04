def dekorator(fun,*args):
    def wewn(*args):
        print('dekoracja')
        fun(*args)
    return wewn

@dekorator
def funkcja(imie):
    print(f'hello {imie}!')

funkcja ("Robert")