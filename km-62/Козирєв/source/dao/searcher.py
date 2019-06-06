from root.dao.db import Database


class EventsSearcher:

    def __init__(self):
        self.db = Database()

    def getEventsData(self, account, priority, planneddate, state):
        query = "select * from table(orm_searcher.GetRequiredEvents({0}, {1}, {2}, {3}))".format(account, priority, planneddate, state)
        result = self.db.execute(query)
        return result.fetchall()


if __name__ == "__main__":
    helper = EventsSearcher()
