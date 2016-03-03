import time
import taskmodel_t as t

if __name__ == "__main__":
    tli = t.TaskIntervalMock(1414675800,5,5)
    tl = t.TaskList(tli)

    tl.start()
    print tl.tasks_for_interval
