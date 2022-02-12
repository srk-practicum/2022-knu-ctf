from cffi import FFI
ffi = FFI()
ffi.set_source("_Android_3", """
unsigned int sub_deadbeef(unsigned int param1, unsigned int param2)
{
    return param1 >> (-param2 & 7) | param1 << (param2 & 0xff) & 0xff;
}

unsigned char sub_100500(unsigned char param1)
{
    return ~param1;
}

unsigned int sub_31337(unsigned int param1, unsigned int param2)
{
    return param1 ^ param2;
}

unsigned int sub_c0ffee(unsigned int param1, unsigned int param2)
{
    return sub_deadbeef(param1, 8 - param2);
}
""")
ffi.cdef("""unsigned int sub_deadbeef(unsigned int, unsigned int);""")
ffi.cdef("""unsigned char sub_100500(unsigned char);""")
ffi.cdef("""unsigned int sub_31337(unsigned int, unsigned int);""")
ffi.cdef("""unsigned int sub_c0ffee(unsigned int, unsigned int);""")
ffi.compile()