#include <pygobject.h>
#include <libgda/libgda.h>

#ifndef PYGDA_VALUE_CONVERSIONS_H
#define PYGDA_VALUE_CONVERSIONS_H

G_BEGIN_DECLS

int
pygda_value_from_pyobject(GValue *boxed, PyObject *input);

PyObject *
pygda_value_as_pyobject(const GValue *value, gboolean copy_boxed);

G_END_DECLS

#endif //PYGDA_VALUE_CONVERSIONS_H
