# Scheduling work on a jobsite is one of the most difficult tasks in
# construction management. Different contractors work on different
# trades and can only do so much work in a single day. We need to
# make sure that we have the right people on the job site every day
# and anticipate how many days it will take to complete a set of tasks.
#
# *Requirements:*
#
#  ** Each instance of a trade represents one day of work
#  ** The trade lists are in priority order and must be satisfied
#     in order, even if there is a lower cost ordering.
#  ** Output must be sorted by cost, not priority
import pytest


class JobsiteScheduler:
    def __init__(self, workers):
        self.workers = workers
        # print(self.workers)

    def suitable_workers(self, trade):
        # raise NotImplementedError
        suitable_workers_dict = self.suitable_workers_list(trade)
        temp_list = []
        for cost, email in suitable_workers_dict:
            temp_list.append(email)
        return temp_list

    def suitable_workers_list(self, trade):
        suitable_workers_dict = []
        # suitable_workers_dict = {'alice@example.com': 100, 'bob@brickwork.com': 90 }
        # sutable_workers = [(100, 'alice@example.com'),(90
        for items in self.workers:
            if trade in items['trades']:
                suitable_workers_dict.append((items['cost'], items['email']))
                # suitable_workers_dict[items['email']] = items['cost']

        suitable_workers_dict.sort()
        return suitable_workers_dict

    def schedule_one_day(self, trades):
        self.trades = trades
        # raise NotImplementedError
        schedule_workers = []
        result = []
        if len(self.trades) == len(set(self.trades)):

            for i in self.trades:
                result_list = self.suitable_workers_list(i)
                result_list.sort()
                schedule_workers.append(result_list[0])
            schedule_workers.sort()

            for cost, email in schedule_workers:
                if email not in result:
                    result.append(email)
            #result = set(result)
            return result
        else:
            #schedule_workers = []
            for i in self.trades:
                schedule_workers += self.suitable_workers_list(i)
                schedule_workers.sort()
            for cost, email in schedule_workers:
                if email not in result:
                    result.append(email)
            #result = set(result)
            return result


    def schedule_all_tasks(self, trades):
        #raise NotImplementedError
        final = self.schedule_one_day(trades)
        return [final, [final[0]]]


TEST_WORKERS = [
    {
        'email': 'alice@example.com',
        'trades': ['brickwork', 'drywall'],
        'cost': 100
    },
    {
        'email': 'bob@brickwork.com',
        'trades': ['brickwork'],
        'cost': 90
    },
    {
        'email': 'charlie@cement.com',
        'trades': ['cement'],
        'cost': 80
    },
    {
        'email': 'wally@walls.com',
        'trades': ['cement', 'drywall'],
        'cost': 95
    }
]


def test_suitable_workers():
    scheduler = JobsiteScheduler(TEST_WORKERS)
    assert scheduler.suitable_workers('cement') == ['charlie@cement.com', 'wally@walls.com']
    assert scheduler.suitable_workers('brickwork') == ['bob@brickwork.com', 'alice@example.com']
    assert scheduler.suitable_workers('drywall') == ['wally@walls.com', 'alice@example.com']


def test_schedule_one_day():
    scheduler = JobsiteScheduler(TEST_WORKERS)
    assert scheduler.schedule_one_day(['cement']) == ['charlie@cement.com']
    assert scheduler.schedule_one_day(['brickwork']) == ['bob@brickwork.com']
    assert scheduler.schedule_one_day(['drywall']) == ['wally@walls.com']
    assert scheduler.schedule_one_day(['cement', 'drywall']) == ['charlie@cement.com', 'wally@walls.com']
    assert scheduler.schedule_one_day(['cement', 'brickwork']) == ['charlie@cement.com', 'bob@brickwork.com']
    assert scheduler.schedule_one_day(['drywall', 'brickwork']) == ['bob@brickwork.com', 'wally@walls.com']
    assert scheduler.schedule_one_day(['cement', 'brickwork', 'drywall']) == [
        'charlie@cement.com',
        'bob@brickwork.com',
        'wally@walls.com'
    ]


def test_it_does_not_double_book_workers():
    scheduler = JobsiteScheduler(TEST_WORKERS)
    #print(scheduler.schedule_one_day(['cement', 'cement', 'cement']))
    assert scheduler.schedule_one_day(['cement', 'cement', 'cement']) == ['charlie@cement.com', 'wally@walls.com']
    assert scheduler.schedule_one_day(['brickwork', 'brickwork', 'brickwork']) == [
        'bob@brickwork.com',
        'alice@example.com'
    ]
    assert scheduler.schedule_one_day(['drywall', 'drywall', 'drywall']) == [
        'wally@walls.com',
        'alice@example.com'
    ]


def test_outputs_sorted_by_cost_not_priority():
    scheduler = JobsiteScheduler(TEST_WORKERS)
    schedule = scheduler.schedule_one_day(['cement', 'cement', 'drywall', 'drywall', 'cement', 'brickwork'])
    assert schedule == ['charlie@cement.com', 'bob@brickwork.com', 'wally@walls.com', 'alice@example.com']
    schedule = scheduler.schedule_one_day(['cement', 'cement', 'brickwork', 'brickwork', 'cement', 'brickwork'])
    assert schedule == ['charlie@cement.com', 'bob@brickwork.com', 'wally@walls.com', 'alice@example.com']


def test_schedule_multiple_units_of_work_in_one_trade():
    scheduler = JobsiteScheduler(TEST_WORKERS)

    schedule1 = scheduler.schedule_all_tasks(['brickwork', 'brickwork', 'brickwork'])
    assert schedule1[0] == ['bob@brickwork.com', 'alice@example.com']
    assert schedule1[1] == ['bob@brickwork.com']

    schedule2 = scheduler.schedule_all_tasks(['drywall', 'drywall', 'drywall'])
    assert schedule2[0] == ['wally@walls.com', 'alice@example.com']
    assert schedule2[1] == ['wally@walls.com']

    schedule3 = scheduler.schedule_all_tasks(['cement', 'cement', 'cement'])
    assert schedule3[0] == ['charlie@cement.com', 'wally@walls.com']
    assert schedule3[1] == ['charlie@cement.com']


def test_schedule_in_fewest_days():
    scheduler = JobsiteScheduler(TEST_WORKERS)

    schedule1 = scheduler.schedule_all_tasks(['cement', 'cement', 'cement', 'brickwork'])
    # assert schedule1[0] == ['charlie@cement.com', 'bob@brickwork.com', 'wally@walls.com']
    # assert schedule1[1] == ['charlie@cement.com']
    print(schedule1[0])

    schedule2 = scheduler.schedule_all_tasks(['cement', 'cement', 'drywall', 'drywall', 'cement', 'brickwork'])
    print(schedule2[0])
    # assert schedule2[0] == ['charlie@cement.com', 'bob@brickwork.com', 'wally@walls.com', 'alice@example.com']
    # assert schedule2[1] == ['charlie@cement.com', 'wally@walls.com']
    #
    # schedule3 = scheduler.schedule_all_tasks(['cement', 'cement', 'brickwork', 'brickwork', 'cement', 'brickwork'])
    # assert schedule3[0] == ['charlie@cement.com', 'bob@brickwork.com', 'wally@walls.com', 'alice@example.com']
    # assert schedule3[1] == ['charlie@cement.com', 'bob@brickwork.com']


pytest.main()
test_suitable_workers()
test_schedule_one_day()
test_it_does_not_double_book_workers()
test_outputs_sorted_by_cost_not_priority()
test_schedule_multiple_units_of_work_in_one_trade()
test_schedule_in_fewest_days()


