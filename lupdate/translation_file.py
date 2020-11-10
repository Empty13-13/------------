# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import os
from xml.etree import ElementTree

from .user import User, UserException


class TranslationFile(User):
    """ Encapsulate a translation file. """

    def __init__(self, ts_file, **kwargs):
        """ Initialise the translation file. """

        super().__init__(**kwargs)

        if os.path.isfile(ts_file):
            self.progress("Reading {0}...".format(ts_file))

            try:
                self._root = ElementTree.parse(ts_file).getroot()
            except Exception as e:
                raise UserException(
                        "{}: {}: {}".format(ts_file,
                                "invalid translation file", str(e)))
        else:
            self._root = ElementTree.fromstring(_EMPTY_TS)

        self._ts_file = ts_file

        # Create a dict of contexts keyed by the context name and having the
        # 2-tuple of the context element and the list of message elements as
        # the value.
        self._contexts_dict = {}

        for context_el in self._root:
            if context_el.tag != 'context':
                continue

            name = ''
            message_els = []

            for el in context_el:
                if el.tag == 'name':
                    name = el.text
                elif el.tag == 'message':
                    message_els.append(el)

            if name != '':
                self._contexts_dict[name] = (context_el, message_els)

    def update(self, source):
        """ Update the translation file from a SourceFile object. """

        self.progress(
                "Updating {0} from {1}...".format(self._ts_file,
                        source.filename))

        for context in source.contexts:
            try:
                context_el, message_els = self._contexts_dict[context.name]
            except KeyError:
                # Create a new context element.
                context_el = ElementTree.Element('context')
                name_el = ElementTree.Element('name')
                name_el.text = context.name
                context_el.append(name_el)
                self._root.append(context_el)

                message_els = []
                self._contexts_dict[context.name] = (context_el, message_els)

                self.progress("Added new context '{0}'".format(context.name))

            for message in context.messages:
                this_message_el = None
                location_el = None
                comment_el = None
                extracomment_el = None
                extra_els = []

                for message_el in message_els:
                    for el in message_el:
                        if el.tag == 'location':
                            location_el = el
                        elif el.tag == 'source':
                            if el.text == message.source:
                                this_message_el = message_el
                        elif el.tag == 'comment':
                            comment_el = el
                        elif el.tag == 'extracomment':
                            extracomment_el = el
                        elif el.tag.startswith('extra-'):
                            extra_els.append(el)

                if this_message_el is None:
                    # Create a new message element.

                    attrs = {}

                    if message.embedded_comments.message_id:
                        attrs['id'] = message.embedded_comments.message_id

                    if message.numerus:
                        attrs['numerus'] = 'yes'

                    message_el = ElementTree.Element('message', attrs)

                    message_el.append(self._make_location_el(message))

                    source_el = ElementTree.Element('source')
                    source_el.text = message.source
                    message_el.append(source_el)

                    comment_el = self._make_comment_el(message)
                    if comment_el is not None:
                        message_el.append(comment_el)

                    extracomment_el = self._make_extracomment_el(message)
                    if extracomment_el is not None:
                        message_el.append(extracomment_el)

                    translation_el = ElementTree.Element('translation',
                            type='unfinished')

                    if message.numerus:
                        translation_el.append(ElementTree.Element(
                                'numerusform'))

                    message_el.append(translation_el)

                    self._add_extras(message, message_el)

                    message_els.append(message_el)
                    context_el.append(message_el)

                    self.progress(
                            "Added new message '{0}'".format(
                                    self.pretty(message.source)))
                else:
                    # Update the existing message element.

                    if location_el is not None:
                        this_message_el.remove(location_el)

                    if comment_el is not None:
                        this_message_el.remove(comment_el)

                    if extracomment_el is not None:
                        this_message_el.remove(extracomment_el)

                    for extra_el in extra_els:
                        this_message_el.remove(extra_el)

                    this_message_el.set('id',
                            message.embedded_comments.message_id)
                    this_message_el.set('numerus',
                            'yes' if message.numerus else 'no')

                    comment_el = self._make_comment_el(message)
                    if comment_el is not None:
                        this_message_el.insert(0, comment_el)

                    extracomment_el = self._make_extracomment_el(message)
                    if extracomment_el is not None:
                        this_message_el.insert(0, extracomment_el)

                    this_message_el.insert(0, self._make_location_el(message))

                    self._add_extras(message, this_message_el)

                    self.progress(
                            "Updated message '{0}'".format(
                                    self.pretty(message.source)))

    def write(self):
        """ Write the translation file back to the filesystem. """

        # Sort the contexts.
        self._root[:] = sorted(self._root, key=lambda el: el.find('name').text)

        self.progress("Writing {0}...".format(self._ts_file))
        with open(self._ts_file, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<!DOCTYPE TS>\n')

            ElementTree.ElementTree(self._root).write(f, encoding='unicode')
            f.write('\n')

    @staticmethod
    def _add_extras(message, message_el):
        """ Add any 'extra-' elements to a message element. """

        for field, value in message.embedded_comments.extras:
            el = ElementTree.Element('extra-' + field)
            el.text = value
            message_el.append(el)

    @staticmethod
    def _make_comment_el(message):
        """ Return a 'comment' element. """

        if not message.comment:
            return None

        el = ElementTree.Element('comment')
        el.text = message.comment

        return el

    @staticmethod
    def _make_extracomment_el(message):
        """ Return an 'extracomment' element. """

        if not message.embedded_comments.extra_comments:
            return None

        el = ElementTree.Element('extracomment')
        el.text = ' '.join(message.embedded_comments.extra_comments)

        return el

    def _make_location_el(self, message):
        """ Return a 'location' element. """

        return ElementTree.Element('location',
                filename=os.path.relpath(message.filename,
                        start=os.path.dirname(os.path.abspath(self._ts_file))),
                line=str(message.line_nr))


# The XML of an empty .ts file.  This is what a current lupdate will create
# with an empty C++ source file.
_EMPTY_TS = '''<TS version="2.1">
</TS>
'''
