import argtypes

class GValueArg(argtypes.ArgType):
    def write_param(self, ptype, pname, pdflt, pnull, info):
        info.varlist.add('GValue', pname + ' = { 0 }')
        info.varlist.add('PyObject', '*py_' + pname)
        info.codebefore.append('    pygda_value_from_pyobject(&%s, py_%s);\n' % (pname, pname))
        info.codeafter.append('    if(G_IS_VALUE(&%s)) g_value_unset(&%s);\n' % (pname, pname))
        info.arglist.append('&' + pname)
        info.add_parselist('O', ['&py_' + pname], [pname])

    def write_return(self, ptype, ownsreturn, info):
        if(ptype == 'const-GValue*'):
            info.varlist.add('const GValue', '*ret')
        else:
            info.varlist.add('GValue', '*ret')
        info.varlist.add('PyObject', '*pyret')

        info.codeafter.append('    pyret = pygda_value_as_pyobject(ret, TRUE);\n')
        if ownsreturn:
            info.codeafter.append('    if(G_IS_VALUE(ret)) g_value_unset(ret);\n')
        info.codeafter.append('    return pyret;')

arg = GValueArg()
argtypes.matcher.register('GValue*', arg)
argtypes.matcher.register('const-GValue*', arg)
