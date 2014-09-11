import json, random, string

class DataTables():

    __source = None

    __paginationType = "full_numbers"

    __columns = []

    __html = ''

    __tableClass = ""

    __tableID = "DataTable-2014"

    __mData = []

    def __init__(self, tableClass = "table", paginationType = "full_numbers", source = None):

        self.__tableClass = tableClass

        self.__paginationType = paginationType

        self.__tableID = random.choice(string.ascii_uppercase)

        if not source:
            raise Exception("Invalid data source exception.")
        else:
            self.__source = source


    def setColumns(self, columns):

        self.__columns = columns

    def __renderColumns(self):

        html = '\n<colgroup>\n'
        cout = 0
        for i in self.__columns:
            html += '  <col class="con' + str(cout) + '" />\n'
            cout += 1
        html += '</colgroup>\n'
        html += '<thead>\n   <tr>\n'

        for i in self.__columns:
            html += '       <th align="center" valign="middle" class="head' + i.keys()[0] + '">' + i.values()[0] + '</th>\n'

            self.__mData.append({"mData":str(i.keys()[0])})

        html += '  </tr>\n </thead>\n'

        return html

    def __renderTable(self):
        table = '<table class="dataTable ' + self.__tableClass + '" id="'+ self.__tableID +'">'
        table += self.__renderColumns()
        table += ' <tbody></tbody>\n</table>\n'
        return table

    def __renderScript(self):
        javascript = '<script type="text/javascript">\njQuery(document).ready(function(){\n'
        javascript += '   oTable = jQuery("#' + self.__tableID + '").dataTable({\n'
        javascript += '      "sPaginationType": "' + self.__paginationType + '",\n'
        javascript += '      "bProcessing": false,\n'
        javascript += '      "sAjaxSource": "' + self.__source + '",\n'
        javascript += '      "bServerSide": true,\n'
        javascript += '      "aoColumns": ' + json.dumps(self.__mData)
        javascript += '\n   }); \n}); \n</script>'
        return javascript

    def render(self):
        html = self.__renderTable()
        html += self.__renderScript()
        return html


class Collections():

    # @var data list
    data = []

    # @var list columns - The actual columns of the data
    __columns = []

    # list of columns that will rendered to JSON
    __showColumns = []

    # Data Template
    template = {
        "aaData" : [],
        "sEcho":0,
        "iTotalRecords":0,
        "iTotalDisplayRecords":0
    }

    # Accept the data from the constructor
    def __init__(self, data):

        self.data = data
        self.__getColumns(self.data)

    # Get the data keys as default columns
    def __getColumns(self, data):

        self.__columns = data[0].keys()

        return None

    # Sets the user defined columns
    # If columns doesnt exists it will be ignored
    def setColumns(self, columns):

        self.__showColumns = columns

    def __formatData(self, data):

        columns = self.__validateColumns()
        for dt in data:
            dict = {}
            for cl in columns:
                dict[cl] = dt[cl]
            self.template["aaData"].append(dict)

        self.template["sEcho"] = 1
        self.template["iTotalRecords"] = len(data)
        self.template["iTotalDisplayRecords"] = len(data)

        return self.template


    def __validateColumns(self):

        if not self.__showColumns:

            return self.__columns

        else:
            valid = []
            for i in self.__showColumns:
                if i in self.__columns:
                    valid.append(i)

            return valid


    # Return all data in JSON Format
    def respond(self):
        data = self.__formatData(self.data)
        return json.dumps(data)






