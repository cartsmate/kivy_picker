import time
import random
import psycopg2
import pandas as pd
from threading import Thread, Lock, current_thread
from sqlalchemy.engine import URL


class MultiThreadingPub:

    # # # # # # # # # # # # # # # # # # # # # # #
    # # # Threading with database queries # # #
    # # # # # # # # # # # # # # # # # # # # #
    def __init__(self):
        self.db_conn = psycopg2.connect(
                database="deb2u2ehdm8ih3",
                user="bjoonismanuyqb",
                password="42c662ab36a741716575f3e0101741349280622fff71ce246b15410de5c460d6",
                host="ec2-54-76-132-202.eu-west-1.compute.amazonaws.com",
                port='5432'
            )
        self.url = URL.create(
                drivername='postgresql',
                database="deb2u2ehdm8ih3",
                username="bjoonismanuyqb",
                password="42c662ab36a741716575f3e0101741349280622fff71ce246b15410de5c460d6",
                host="ec2-54-76-132-202.eu-west-1.compute.amazonaws.com",
                port=5432
                )

    def query_pub_record(self, sql):
        curs_obj = self.db_conn.cursor()
        curs_obj.execute("""SELECT column_name  
                                        FROM information_schema.columns 
                                        WHERE table_schema = 'thepubpicker' 
                                        AND
                                        table_name = 'pub_record' """)
        result = curs_obj.fetchall()
        table_headers = []
        for res in result:
            table_headers.append(res[0])

        # filter = round(random.uniform(4.1, 4.9), 1)
        # print('filter', filter)
        # sql = f"select * from thepubpicker.pub_record d where ranking = '{filter}' order by detail_name limit 10"
        # print('sql', sql)
        # # curs_obj.execute(f"""select * from thepubpicker.pub_record d where ranking == {filter} limit 10 order by detail_name""")

        curs_obj.execute(sql)
        result = curs_obj.fetchall()
        print('result', result)
        global df_pub_record
        df_pub_record = pd.DataFrame(result, columns=table_headers)

    def query_daily_event(self):
        curs_obj = self.db_conn.cursor()
        curs_obj.execute("""SELECT column_name  
                            FROM information_schema.columns 
                            WHERE table_schema = 'thepubpicker' 
                            AND
                            table_name = 'daily_event' """)
        result = curs_obj.fetchall()
        table_headers = []
        for res in result:
            table_headers.append(res[0])
        curs_obj.execute("""select * from thepubpicker.daily_event evnt limit 10""")
        result = curs_obj.fetchall()
        global df_daily_event
        df_daily_event = pd.DataFrame(result, columns=table_headers)

    def thread_caller(self, sql):
        start = time.process_time()
        thread6 = Thread(target=self.query_daily_event)
        thread7 = Thread(target=self.query_pub_record(sql))

        thread6.start()
        thread7.start()

        thread6.join()
        thread7.join()

        # df_dict = {"df_daily_event": df_daily_event,
        df_dict = { "df_pub_record": df_pub_record }

        print(time.process_time() - start)

        return df_dict


# # # # # # # # # # # # # # #
# # # EXAMPLE of queue # # #
# # # # # # # # # # # # # #
# def worker(q, lock):
#     while True:
#         value = q.get()
#         with lock:
#             print(f'in {current_thread().name} got {value}')
#         q.task_done()
#
#
# if __name__ == '__main__':
#     q = Queue()
#     lock = Lock()
#     num_threads = 10
#
#     for i in range(num_threads):
#         thread = Thread(target=worker, args=(q, lock))
#         thread.daemon = True
#         thread.start()
#
#     for i in range(1, 21):
#         q.put(i)
#
#     q.join()
#
#     print('end main')


# # # # # # # # # # # # # # # # # #
# # # syntax of using QUEUES # # #
# # # # # # # # # # # # # # # #
# if __name__ == '__main__':
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)
#
#     # 3, 2, 1 -->
#     first = q.get()
#     print(first)
#
#     q.task_done()
#     q.join()
#
#     print('end main')


# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # with EXACT (or KNOWN) number of threads # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# database_value = 0
#
#
# def increase(lock):
#     global database_value
#     # 'context manager'
#     # with lock:
#
#     # or specify acquire and release (same as file open/close)
#     lock.acquire()
#     local_copy = database_value
#     # processing
#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy
#     lock.release()
#
#
# lock = Lock()
# print('start value', database_value)
#
# thread1 = Thread(target=increase, args=(lock,))
# thread2 = Thread(target=increase, args=(lock,))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print('end value', database_value)


# # # TEST SCRIPT # # #

# def db_query_1():
#     con = psycopg2.connect(
#         database="deb2u2ehdm8ih3",
#         user="bjoonismanuyqb",
#         password="42c662ab36a741716575f3e0101741349280622fff71ce246b15410de5c460d6",
#         host="ec2-54-76-132-202.eu-west-1.compute.amazonaws.com",
#         port='5432'
#     )
#     curs_obj = con.cursor()
#     curs_obj.execute("""select * from thepubpicker.detail d """)
#
#
# def db_query_2():
#     con = psycopg2.connect(
#         database="deb2u2ehdm8ih3",
#         user="bjoonismanuyqb",
#         password="42c662ab36a741716575f3e0101741349280622fff71ce246b15410de5c460d6",
#         host="ec2-54-76-132-202.eu-west-1.compute.amazonaws.com",
#         port='5432'
#     )
#     curs_obj = con.cursor()
#     curs_obj.execute("""select * from thepubpicker.review r """)


#
# def square_numbers():
#     for i in range(100):
#         i * i
#
# threads = []
# num_threads = 0
#
# for i in range(num_threads):
#     thread = Thread(target=square_numbers)
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print('end threading')
