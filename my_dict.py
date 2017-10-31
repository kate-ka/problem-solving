class mydict(dict):
    no = 'cat'

    # def __getattr__(self, key):
    #     try:
    #         return super(mydict, self).__getattr__(key)
    #     except Exception as e:
    #         print ('cat')
    #         return self[key]
    '''If you need to catch every attribute regardless whether it exists or not, use __getattribute__ instead.

    __getattr__ only gets called for attributes that don't actually exist.
    If you set the attribute directly, referencing that attribute will retrieve it without calling __getattr__.

    __getattribute__ is called all the times.'''


    # def __getattribute__(self, key):
    #     return self[key]

    def __getattr__(self, key):
         return self[key]

    def __setattr__(self, key, value):
        self[key] = value



a = mydict(no = "way", bad = "code")
a.no = 'fway'
# print a.no
a.update({1:"one", 2:"two" , 'test': 5})
# print a.no
print a.no
# print a.test

