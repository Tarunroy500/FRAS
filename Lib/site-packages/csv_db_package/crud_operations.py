"""The script contains different functions for CRUD operations in database."""

import logging
import os
from mysql.connector import connect, errors

logging.basicConfig(filename='server_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


config = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': 'user_data'
}


def view_data(db_name: str, db_table: str):
    """The function creates the data table when the file was uploaded on the browser.
        :param - database name in string format
        :param - database table name in string format
        :return - a table format of file uploaded on browser itself."""
    try:
        if db_name is not None and db_table is not None:
            conn = connect(**config)

            if conn.is_connected():
                cursor = conn.cursor()

                cursor.execute(f"SELECT * FROM {db_name}.{db_table}")
                columns = cursor.column_names
                data = cursor.fetchall()
                conn.close()
                count = 0
                html_table = ''
                html_table += '<table><tr>'
                for i in range(len(columns)):
                    html_table += f'<th id="thead_{i}">{columns[i]}</th>'
                html_table += '<td><button type="submit"' \
                              ' onclick="redirect_to_create()">Create</button></td>'
                html_table += '</tr>'
                for rows in range(len(data)):
                    html_table += f'<tr id={rows}>'
                    for item in range(len(data[rows])):
                        html_table += f'<td class="row-data"> {data[rows][item]} </td>'
                    html_table += '<td><button type="button" ' \
                                  'onclick="my_button_click_handler()">Delete</button>'
                    html_table += '</td>'
                    html_table += '<td><button type="submit"' \
                                  ' onclick="my_update_data()">Update</button></td>'
                    html_table += '</tr>'
                    count += 1
                html_table += '</table>'

            return html_table, count
        return f"Db {db_name} or Table {db_table} doesn't exist"

    except errors.ProgrammingError as db_e:
        logging.error('%s: %s', db_e.__class__.__name__, db_e)
        raise
    except errors.Error as err:
        logging.error('%s: %s', err.__class__.__name__, err)
        raise



def delete_row(db_name: str, db_table: str, p_id):
    """The function deletes the row from the database by pressing delete button from browser.
        :param - database name in string format
        :param - database table name in string format
        :param - p_id which user want to delete
        :return - show the table by removing the particular row"""
    try:
        if db_name is not None and db_table is not None:
            conn = connect(**config)

            if conn.is_connected():
                cursor = conn.cursor()

                cursor.execute(f"DELETE FROM {db_name}.{db_table} WHERE p_id={p_id}")
                conn.commit()
                conn.close()
            return "Deleted Successfully"
        return None
    except errors.ProgrammingError as db_e:
        logging.error('%s: %s', db_e.__class__.__name__, db_e)
        raise
    except errors.Error as err:
        logging.error('%s: %s', err.__class__.__name__, err)
        raise


def insert_row(db_name: str, db_table: str, dict_values: dict):
    """
    The function insert the new row to the database.
    :param db_name:
    :param db_table:
    :param dict_values:
    :return:
    """
    try:
        if db_name is not None and db_table is not None:
            conn = connect(**config)

            if conn.is_connected():
                cursor = conn.cursor(buffered=True)
                columns = list(dict_values.keys())
                columns = ','.join(columns)
                values = [dict_values[col] for col in dict_values]
                cursor.execute(f"INSERT INTO {db_name}.{db_table} "
                               f"({columns}) VALUES {tuple(values)}")
                conn.commit()
            return "Successfully Inserted"
        return None
    except errors.IntegrityError as in_err:
        logging.error('%s: %s', in_err.__class__.__name__, in_err)
        raise
    except errors.ProgrammingError as db_err:
        logging.error('%s: %s', db_err.__class__.__name__, db_err)
        raise
    except errors.Error as err:
        logging.error('%s: %s', err.__class__.__name__, err)
        raise


def update_row(db_name: str, db_table: str, dict_values: dict, p_id):
    """The function updates the row from the database by pressing update button from browser.
            :param - database name in string format
            :param - database table name in string format
            :param - dictionary of all values of a particular row selected by the user
            :param - p_id which user want to delete
            :return - show the table by updating the particular row"""
    try:
        if db_name is not None and db_table is not None:
            conn = connect(**config)

            if conn.is_connected():
                cursor = conn.cursor()
                d_values = [f"{key}" + "=" + f"'{dict_values[key]}'" for key in dict_values]
                join_values = ','.join(d_values)
                cursor.execute(f"UPDATE {db_name}.{db_table} SET {join_values} WHERE p_id={p_id}")

                conn.commit()
                conn.close()
            return "data updated successfully"
        return None
    except errors.IntegrityError as in_err:
        logging.error('%s: %s', in_err.__class__.__name__, in_err)
        raise
    except errors.ProgrammingError as db_e:
        logging.error('%s: %s', db_e.__class__.__name__, db_e)
        raise
    except errors.Error as err:
        logging.error('%s: %s', err.__class__.__name__, err)
        raise


def select_row(db_name: str, db_table: str, p_id):
    """The function is used to get the row from the database by pressing update
        for the prefilling of the data to the new page to update it.
            :param - database name in string format
            :param - database table name in string format
            :param - p_id which user want to update
            :return - show the prefilled form on the new page to update the data"""
    try:
        if db_name is not None and db_table is not None:
            conn = connect(**config)

            output = ''
            if conn.is_connected():
                cursor = conn.cursor()

                cursor.execute(f"SELECT * FROM {db_name}.{db_table} WHERE p_id={p_id}")
                columns = cursor.column_names
                value = cursor.fetchone()

                for i in range(len(columns)):
                    output += f'{columns[i]} <input name="{columns[i]}" ' \
                              f'type="text" value="{value[i]}"><br>'
                output += '<button type="submit" onclick="redirect_to_viewtable()">Update</button>'
                conn.close()

            return output
        return None
    except errors.DatabaseError as db_e:
        logging.error('%s: %s', db_e.__class__.__name__, db_e)
        raise
    except errors.Error as err:
        logging.error('%s: %s', err.__class__.__name__, err)
        raise
