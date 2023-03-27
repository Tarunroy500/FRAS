"""The script to create a http server on local for uploading a csv file
    and perform CRUD operations on the UI connected with the database."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import logging
import jinja2
from mysql.connector import connect, errors
import pandas as pd
from crud_operations import view_data, delete_row, insert_row, select_row, update_row


logging.basicConfig(filename='server_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

CREATE_TABLE_QUERY = """
                        CREATE TABLE user_file_data(p_id int PRIMARY KEY, first_name varchar(255),height_feet float,
                        height_inches float, last_name varchar(255),position varchar(255),weight_pounds float,id int,
                        abbreviation varchar(255),city varchar(255), conference varchar(255), division varchar(255),
                        full_name varchar(255), name varchar(255))
                     """


def csv_to_db(file_name):
    """The function reads a file that was uploaded by the user to the server.
        It creates connection to the database and that file was dumped to the database.
        : param - csv file uploaded by the user."""

    data_frame = pd.read_csv(file_name, index_col=False, delimiter=',')
    replacement = {'height_feet': 0.0, 'height_inches': 0.0,
                   'position': "missing", 'weight_pounds': 0.0}
    data_frame.fillna(value=replacement, inplace=True)
    data_frame.fillna(0, inplace=True)
    try:
        conn = connect(host='localhost',
                       database="user_data",
                       user='root',
                       password='Arp@99?0#1Liy@')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logging.info("You're connected to database: %s", record)
            cursor.execute('DROP TABLE IF EXISTS user_file_data;')
            logging.info('Creating table....')

            cursor.execute(CREATE_TABLE_QUERY)
            logging.info("Table is created....")
            # loop through the data frame
            for i, row in data_frame.iterrows():
                cursor.execute(f"INSERT INTO user_data.user_file_data VALUES {tuple(row)}")
                conn.commit()
    except errors.ProgrammingError as prmg_err:
        logging.error('%s: %s', prmg_err.__class__.__name__, prmg_err)
    except errors.Error as err_e:
        logging.error('%s: %s', err_e.__class__.__name__, err_e)


class EchoHandler(BaseHTTPRequestHandler):
    """class containing different GET and POST methods for the http server that was used
        to upload a csv file from the user. Then the CRUD operations is performed on the UI
        as per the user wants to do with a connection to a database."""

    def do_GET(self):
        """Function to upload file and perform CRUD operations on client side."""
        try:
            if self.path.endswith('/uploadCSV'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                with open('Templates/index.html', 'r', encoding='utf-8') as index_file:
                    output = index_file.read()
                self.wfile.write(output.encode())

            if self.path.endswith('/new'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                with open('Templates/upload_file.html', 'r', encoding='utf-8') as uploaded_file:
                    output = uploaded_file.read()
                self.wfile.write(output.encode())

            if self.path.endswith('/viewtable'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                table = view_data('user_data', 'user_file_data')[0]
                if table is not None:
                    with open('Templates/view_table.html', 'r', encoding='utf-8') as view_file:
                        output = view_file.read()
                    render_output = jinja2.Template(output)
                self.wfile.write(render_output.render(table=table).encode())

            if self.path.endswith('/add'):
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                with open('Templates/add_data.html', 'r', encoding='utf-8') as add_file:
                    output = add_file.read()
                self.wfile.write(output.encode())

            if self.path.startswith('/update_data'):
                value = self.path[21:]

                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                row_form = select_row('user_data', 'user_file_data', int(value))
                if row_form is not None:
                    with open('Templates/update_data.html', 'r', encoding='utf-8') as update_file:
                        output = update_file.read()
                    render_output = jinja2.Template(output)
                self.wfile.write(render_output.render(row_form=row_form).encode())

        except PermissionError as per_err:
            logging.error('%s: %s', per_err.__class__.__name__, per_err)
        except TypeError as type_err:
            logging.error('%s: %s', type_err.__class__.__name__, type_err)

    def do_POST(self):
        """Function to upload data to db and returns table and perform CRUD operations."""
        try:
            if self.path.endswith('/new'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT_LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    file = fields.get('task')[0]
                    file = file.decode("utf-8")
                    with open('uploaded_file/file.csv', mode='w', encoding='utf-8') as csv_file:
                        for data in file.split('\r\r'):
                            csv_file.write(data)
                    csv_to_db('file.csv')
                self.send_response(301)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/viewtable')
                self.end_headers()
                self.wfile.write(file.encode())

            if self.path.startswith('/delete_data'):
                value_id = self.path[22:]
                delete_row('user_data', 'user_file_data', value_id)
                self.send_response(301)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/viewtable')
                self.end_headers()

            if self.path.endswith('/add'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT_LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    for key in fields:
                        fields[key] = fields[key][0]
                    insert_row('user_data', 'user_file_data', fields)

                self.send_response(301)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/viewtable')
                self.end_headers()

            if self.path.startswith('/update_data'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                content_len = int(self.headers.get('Content-length'))
                pdict['CONTENT_LENGTH'] = content_len
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    for key in fields:
                        fields[key] = fields[key][0]
                    update_row('user_data', 'user_file_data', fields, int(fields['p_id']))

                self.send_response(301)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/viewtable')
                self.end_headers()
        except PermissionError as per_err:
            logging.error('%s: %s', per_err.__class__.__name__, per_err)
        except TypeError as type_err:
            logging.error('%s: %s', type_err.__class__.__name__, type_err)


def main():
    """The main function creates a server on defined port with the help of http.server package."""
    port = 8000
    server = HTTPServer(('', port), EchoHandler)
    logging.info('Server running on port %s', port)
    server.serve_forever()


if __name__ == '__main__':
    main()
