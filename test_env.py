'''
Filename: /Users/rh01/deeprm/lib/test_env.py
Path: /Users/rh01/deeprm/lib
Created Date: Thursday, June 13th 2019, 7:48:33 pm
Author: rh01

Copyright (c) 2019 Your Company
'''

import unittest


class TestStringMethods(unittest.TestCase):        

    def test_backlog(self):

        from lib.env import Env
        from lib.paramenters import Parameters
        import lib.other_agent as other_agent
        pa = Parameters()
        pa.num_nw = 5
        pa.simu_len = 50
        pa.num_ex = 10
        pa.new_job_rate = 1
        pa.compute_dependent_parameters()

        env = Env(pa, render=False, repre='image')

        env.step(5)
        env.step(5)
        env.step(5)
        env.step(5)
        env.step(5)

        env.step(5)
        # self.assertIsNotNone(env.job_backlog.backlog[0])
        # self.assertIsNone(env.job_backlog.backlog[1])
        print("New job is backlogged.")

        env.step(5)
        env.step(5)
        env.step(5)
        env.step(5)

        job = env.job_backlog.backlog[0]
        env.step(0)
        self.assertEqual(env.job_slot.slot[0],job )
        # assert env.job_slot.slot[0] == job

        job = env.job_backlog.backlog[0]
        env.step(0)
        self.assertEqual(env.job_slot.slot[0],job )

        # assert env.job_slot.slot[0] == job

        job = env.job_backlog.backlog[0]
        env.step(1)
        self.assertEqual(env.job_slot.slot[1],job )


        job = env.job_backlog.backlog[0]
        env.step(1)
        self.assertEqual(env.job_slot.slot[1],job )
        

        env.step(5)

        job = env.job_backlog.backlog[0]
        env.step(3)
        # self.assertEqual(env.job_slot.slot[3],job )

        print("- Backlog test passed -")


    def test_compact_speed(self):
        from lib.env import Env
        from lib.paramenters import Parameters
        import lib.other_agent as other_agent

        pa = Parameters()
        pa.simu_len = 50
        pa.num_ex = 10
        pa.new_job_rate = 0.3
        pa.compute_dependent_parameters()

        env = Env(pa, render=False, repre='compact')

        import time

        start_time = time.time()
        for i in range(100000):
            a = other_agent.get_sjf_action(env.machine, env.job_slot)
            env.step(a)
        end_time = time.time()
        print("- Elapsed time: ", end_time - start_time, "sec -")


    def test_image_speed(self):
        from lib.env import Env
        from lib.paramenters import Parameters
        import lib.other_agent as other_agent

        pa = Parameters()
        pa.simu_len = 50
        pa.num_ex = 10
        pa.new_job_rate = 0.3
        pa.compute_dependent_parameters()

        env = Env(pa, render=False, repre='image')

        import time

        start_time = time.time()
        for i in range(100000):
            a = other_agent.get_sjf_action(env.machine, env.job_slot)
            env.step(a)
        end_time = time.time()
        print("- Elapsed time: ", end_time - start_time, "sec -")



if __name__ == '__main__':
    unittest.main()