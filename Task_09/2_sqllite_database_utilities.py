import sqlite3 as lite
import argparse
import csv
import logging
from datetime import datetime

arr_column_count = 10

def execute_query(name:object, cur:object):
        sql_file = open(f'{name}')
        sql_as_string = sql_file.read()
        cur.execute(sql_as_string)

def create_sqlite_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()        
        myarray = ['drop_table.sql', 'table_creation.sql', 'index_creation.sql']
        for i in myarray:
            execute_query(str(i), cur)
        LOGGER.info("New table in {db} file was created to store ordered numbers information.".format(db=database_path))
    conn.close()

def save_numbers_to_database(database_path: str, ordered_dict_arr: list):
    """
       Function to save ordered numbers to the db file
             :param database_path: path to find the db file
             :param ordered_dict_arr: array with numbers information for each processed in the current run column
             :return: columns saved to file db
         """
    conn = lite.connect(database_path)
    numb_updates = 0
    numb_inserts = 0
    with conn:
        cur = conn.cursor()
        LOGGER.info("Check that row with appropriate PK already exists --> update or insert rows")
        for dict_attr in ordered_dict_arr:
            sql = "select count(1) from t_ordered_items where ORDERED_ITEMS_SURR_ID=" + str(
                dict_attr['ORDERED_ITEMS_SURR_ID']) + " " \
                                                      " and MEMBER = '" + str(dict_attr['MEMBER']) + "'"

            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                ### SQL which should be executed is created using list comprehension
                sql_file = open("update_table.sql")
                sql_as_string = sql_file.read()
                cur.execute(sql_as_string) 
                numb_updates += 1
            else:
                ### SQL which should be executed just hardcoded / could be read from file as well
                sql = "insert into t_ordered_items (ORDERED_ITEMS_SURR_ID ," \
                      "                             COLUMN1_INT , " \
                      "                             COLUMN2_INT, " \
                      "                             COLUMN3_INT , " \
                      "                             COLUMN4_INT , " \
                      "                             COLUMN5_INT , " \
                      "                             COLUMN6_INT," \
                      "                             COLUMN7_INT, " \
                      "                             COLUMN8_INT," \
                      "                             COLUMN9_INT, " \
                      "                             COLUMN10_INT, " \
                      "                             MEMBER,  " \
                      "                             INSERT_DATE)" \
                      "                 values ('" + str(dict_attr['ORDERED_ITEMS_SURR_ID']) + "' ,'" + dict_attr[
                          'COLUMN1'] + "' ,'" + str(dict_attr['COLUMN2']) + "' ,'" + str(
                    dict_attr['COLUMN3']) + "' ,'" + str(
                    dict_attr['COLUMN4']) + "' ,'" \
                      + str(dict_attr['COLUMN5']) + "' ,'" + str(dict_attr['COLUMN6']) + "' ,'" + str(
                    dict_attr['COLUMN7']) + "' ,'" \
                      + str(dict_attr['COLUMN8']) + "' ,'" + str(dict_attr['COLUMN9']) + "' ,'" + str(
                    dict_attr['COLUMN10']) + "' ,'" + str(dict_attr['MEMBER']) + "' , DATE('now') " + ")"
                numb_inserts += 1
            cur.execute(sql)

        LOGGER.info(
            "Ordered numbers are saved into Database successfully! There were {ins} inserts and {upd} updates.".format(
                ins=numb_inserts, upd=numb_updates))


### TASK 2.1 add procedure which will count rows which were inserted today and will just LOGGING this information
def count_todays_insertions(database_path: str):
    conn = lite.connect(database_path)
    cursor = conn.cursor()    
    sql_file = open("count.sql")
    sql_as_string = sql_file.read()
    count_res = cursor.execute(sql_as_string)    
    for res in count_res:
        print(res[0])
        LOGGER.info("The number of today's insertions was counted successfully! It is: {ins}.".format(ins=res[0]))
    conn.close()
### TASK 2.2 You have only inserts into your table what is the reason ?

def read_table_dict_from_file(file_path: str, fio: str) :
    """
           Function to read ordered numbers from file
                 :param file_path: path to find the db file
                 :return: array with dictionaries [{col1:value1, ...coln:valuen},...{col1:value1N,...coln:valueNN}]
             """
    with open(file_path, "r", newline='') as csvin:
        inarr = []
        fl = csv.reader(csvin, delimiter=',')
        header = next(fl)
        column_len = len(header)
        n = 1
        for line in fl:
            out_dict = {}
            for i in range(column_len):
                out_dict[header[i]] = line[i]
            out_dict['ORDERED_ITEMS_SURR_ID'] = n
            out_dict['MEMBER'] = fio
            n += 1
            inarr.append(out_dict)

    return inarr


if __name__ == "__main__":
    start_dt = datetime.now()

    LOG_FILE_PATH = "log_file_2.txt"

    logging.basicConfig(filename=LOG_FILE_PATH,
                        format='%(asctime)s %(message)s',
                        filemode='w')

    LOGGER = logging.getLogger("Module2_Topic1")
    LOGGER.setLevel(logging.DEBUG)
    LOGGER.info("Start of the Module2_Topic1 read numbers from file and insert into SQLLite db")

    t3parser = argparse.ArgumentParser(
        description='Please provide input file and database file name for ordered values')

    t3parser.add_argument("-file_name", "--name", help="File name in the working directory", default="ordered_file.csv")
    t3parser.add_argument("-db_file_name", "--db_name", help="Database file name in the working directory",
                          default="ordered_numbers.db")
    t3parser.add_argument("-student_fio", "--fio", help="Name+Surname to insert this data into table",
                          default="Student")

    args = t3parser.parse_args()

    file_name = args.name
    db_file_name = args.db_name
    fio = args.db_name

    LOGGER.info("Start creation of {db_fname} sqlite db file".format(db_fname=db_file_name))
    create_sqlite_database(db_file_name)

    arr_dict_ordered_numbers = []

    LOGGER.info("Read ordered numbers from file {fname}".format(fname=file_name))
    arr = read_table_dict_from_file(file_name, fio)

    LOGGER.info("Save ordered numbers into appropriate table")
    save_numbers_to_database(db_file_name, arr)
    
    LOGGER.info("Save counted number of today's insertions")
    count_todays_insertions(db_file_name)

    sdiff_time = datetime.now() - start_dt

    LOGGER.info("Script runtime is {time}".format(time=sdiff_time))
