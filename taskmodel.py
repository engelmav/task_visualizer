from datetime import datetime
import pytz
import time
import math
import psycopg2
class TaskInterval():
    def __init__(self):
        self.set_last_run_epoch()
    def set_last_run_epoch(self):
        self.last_run_epoch = round(time.time()) - (86400*5 - 43200)

class TaskIntervalMock():
    def __init__(self,start_epoch,increment):
        self.last_run_epoch = start_epoch
        self.increment = increment
    def set_last_run_epoch(self):
        self.last_run_epoch = self.last_run_epoch + self.increment

class TaskList():
    def __init__(self):
        self.tz = pytz.timezone('America/New_York')

    def get_tasks_for_interval(self,task_interval):
        # get previous run epoch time
        previous_epoch = task_interval.last_run_epoch
        # re-stamp with current time
        task_interval.set_last_run_epoch()

        date = datetime.fromtimestamp(previous_epoch)
        date = date.strftime('%Y%m%d')

        conn = psycopg2.connect( \
            database="postgres",
            user="rtpost",
            password="5306",
            host=DB_HOST
        )

        cur = conn.cursor()

        query = """
            select round(extract(epoch from persistdate::timestamp))
            ,count(*)
            from post.te_tasks_all a
            join post.te_fix b using (taskref)
            where
            a.domain = 'clsa'
            and a.date = %s
            and b.eventtype in ('1', '2')
            and b.persistdate::timestamp >= to_timestamp( %s ) -- '13:30:00'
            and b.persistdate::timestamp <= to_timestamp( %s ) -- '13:40:00'
            group by 1
            order by 1 asc;
            """
        prev = datetime.fromtimestamp(previous_epoch, self.tz)
        now = datetime.fromtimestamp(task_interval.last_run_epoch) 

        print "Date: " + date
        print "From: " + str(previous_epoch) + " to: " + str(task_interval.last_run_epoch)
        print "From: " + str(prev) + " to: " + str(now)

        cur.execute(query, (date, previous_epoch, task_interval.last_run_epoch) )
        self.tasks_for_interval = cur.fetchall()
        conn.close()

