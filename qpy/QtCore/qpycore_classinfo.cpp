// This contains the implementation of pyqtClassInfo.
//
// Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt6.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


#include <Python.h>

#include <QByteArray>
#include <QHash>

#include "qpycore_api.h"
#include "qpycore_classinfo.h"
#include "qpycore_misc.h"

#include "sipAPIQtCore.h"


// Forward declarations.
extern "C" {static PyObject *decorator(PyObject *self, PyObject *cls);}


// The class info name/values keyed by the class type object.
static QHash<PyObject *, QList<ClassInfo> > class_info_hash;


// Implement the pyqtClassInfo class decorator.
PyObject *qpycore_pyqtClassInfo(PyObject *args, PyObject *kwds)
{
    // Check there are no positional arguments.
    if (PyTuple_Size(args) > 0)
    {
        PyErr_SetString(PyExc_TypeError,
                "QObject.pyqtClassInfo() has no positional arguments");
        return 0;
    }

    // Create the decorator function itself.  We stash the arguments in "self".
    // This may be an abuse, but it seems to be Ok.
    static PyMethodDef deco_method = {
        "_deco", decorator, METH_O, 0
    };

    return PyCFunction_New(&deco_method, kwds);
}


// Return the list on the heap of class info name/values for a class.
QList<ClassInfo> qpycore_pop_class_info_list(PyObject *cls)
{
    QList<ClassInfo> class_info = class_info_hash.take(cls);

    if (class_info.length() > 0)
        Py_DECREF(cls);

    return class_info;
}


// This is the decorator function that saves the class info dict for later
// retrieval.
static PyObject *decorator(PyObject *self, PyObject *cls)
{
    QList<ClassInfo> class_info;
    PyObject *name, *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(self, &pos, &name, &value))
    {
        // Convert the name.
        QByteArray name_ba = qpycore_convert_ASCII(name);
        if (name_ba.isNull())
            return 0;

        // Convert the value.
        QByteArray value_ba = qpycore_convert_ASCII(value);
        if (value_ba.isNull())
            return 0;

        // Add the class info.
        class_info.append(ClassInfo(name_ba, value_ba));
    }

    if (class_info.length() > 0)
    {
        Py_INCREF(cls);
        class_info_hash.insert(cls, class_info);
    }

    // Return the class.
    Py_INCREF(cls);
    return cls;
}
