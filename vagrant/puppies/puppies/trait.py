class Trait(object):

    traitTemplate = '''
                <tr class="trait">
                    <td>{0}</td>
                    <td>
                        {1}
                    </td>
                </tr>'''

    inputTemplate = '''<input type="{0}" name="{1}" form="{2}" value="{3}">'''

    textareaTemplate = '''<textarea name="{0}" form="{1}">{2}</textarea>'''

    selectTemplate = '''<select name="{0}" form="{1}">{2}
                        </select>'''

    optionTemplate = '''
                            <option value="{0}"{1}>{2}</option>'''

    imageTemplate = '''<img src="{0}">'''

    def __init__(self, name, value="", inputType="text", options = None):
        self.name = name
        self.value = value
        self.inputType = inputType
        self.options = options


    def isImage(self):
        return self.inputType == "image"


    def asInputElement(self, formName):
        element = ""

        if self.inputType == "text":
            element = self.inputTemplate.format(
                self.inputType,
                self.name,
                formName,
                self.value
            )
        elif self.inputType == "image":
            element = self.inputTemplate.format(
                "text",
                self.name,
                formName,
                self.value
            )
        elif self.inputType == "date":
            element = self.inputTemplate.format(
                self.inputType,
                self.name,
                formName,
                self.value
            )
        elif self.inputType == "textarea":
            element = self.textareaTemplate.format(
                self.name,
                formName,
                self.value
            )
        elif self.inputType == "select":
            options = ""

            # Compile options first...
            for o in self.options:
                selected = ""

                # The value will be the selected option
                if self.value == o:
                    selected = " selected"

                option = self.optionTemplate.format(
                    o,
                    selected,
                    o.title()
                )

                options += option

            # Now combine the options with the select
            element = self.selectTemplate.format(
                self.name,
                formName,
                options
            )

        return self.traitTemplate.format(self.name.title(), element)


    def asImageElement(self):
        return self.imageTemplate.format(self.value)


    def asOutputElement(self):
        element = self.traitTemplate.format(self.name.title(), self.value)
        return element