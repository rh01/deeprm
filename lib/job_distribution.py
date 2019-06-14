'''
Filename: /Users/rh01/deeprm/lib/job_distribution.py
Path: /Users/rh01/deeprm/lib
Created Date: Thursday, June 13th 2019, 7:11:09 pm
Author: rh01

Copyright (c) 2019 Your Company
'''
import datetime
import numpy as np
import logging


class Dist:
    def __init__(self, num_res, max_nw_size, job_len, logger):
        """
        # TODO

        Parameters:
        ----------------------
        :param num_res: number of resource in the system
        :param max_nw_size: maximum resource request of new work
        :param job_len: maximum duration of new jobs
        """
        self.num_res = num_res  # number of resource in the system
        self.max_nw_size = max_nw_size  # maximum resource request of new work
        self.job_len = job_len  # maximum duration of new jobs

        self.job_small_chance = 0.8  # the change generate small jobs

        # job duration is splited to
        # [job_len_small_lower, job_len_small_upper, job_len_big_lower, job_len_big_upper]
        self.job_len_big_lower = job_len * 2 / 3
        self.job_len_big_upper = job_len

        self.job_len_small_lower = 1
        self.job_len_small_upper = job_len / 5

        # the size of main resource in the system.
        self.dominant_res_lower = max_nw_size / 2
        self.dominant_res_upper = max_nw_size

        self.other_res_lower = 1
        self.other_res_upper = max_nw_size / 5

        ####LOGGING CONFIGURATION
        ## basic config
        self.logger = logger

    def normal_dist(self):
        """
        Note
        --------------
        sample a distribution of a new work resource

        Parameters
        ----------------
        :return:

        Example
        ----------------
        >>> d = Dist(num_res = 4, max_nw_size=10, job_len=10)
        >>> d.normal_dist()

        """
        # new work duration
        nw_len = np.random.randint(1, self.job_len + 1)  # same length in every dimension

        # new work resource size
        nw_size = np.zeros(self.num_res)

        for i in range(self.num_res):
            nw_size[i] = np.random.randint(1, self.max_nw_size + 1)

        return nw_len, nw_size

    def bi_model_dist(self):
        """
        return bi-normal distribution,

        Note:
        -------------

        Parameter:
        -------------
        :return:

        Examples:
        -------------
        >>> d = Dist(num_res = 4, max_nw_size=10, job_len=10)
        >>> d.bi_model_dist()
        1, [2. 9. 2. 2.]
        """

        # -- job length --
        if np.random.rand() < self.job_small_chance:  # small job
            nw_len = np.random.randint(self.job_len_small_lower,
                                       self.job_len_small_upper + 1)
        else:  # big job
            nw_len = np.random.randint(self.job_len_big_lower,
                                       self.job_len_big_upper + 1)

        nw_size = np.zeros(self.num_res)

        # -- job resource request --
        dominant_res = np.random.randint(0, self.num_res)  # dominant resource must be < self.num_res
        for i in range(self.num_res):
            if i == dominant_res:
                nw_size[i] = np.random.randint(self.dominant_res_lower,
                                               self.dominant_res_upper + 1)
            else:
                nw_size[i] = np.random.randint(self.other_res_lower,
                                               self.other_res_upper + 1)

        self.logger.info("Dominat resource is {}, and (nw_len={},nw_size={})" .format(dominant_res, nw_len, nw_size))


        return nw_len, nw_size


def generate_sequence_work(pa, seed=42):
    """
    generate seqence work set

    Parameters
    --------------
    :param pa:
    :param seed:
    :return:
    """
    np.random.seed(seed)

    simu_len = pa.simu_len * pa.num_ex

    nw_dist = pa.dist.bi_model_dist

    # new work duration, many simulated new work
    nw_len_seq = np.zeros(simu_len, dtype=int)
    # resource request of the new work.
    nw_size_seq = np.zeros((simu_len, pa.num_res), dtype=int)

    for i in range(simu_len):
        if np.random.rand() < pa.new_job_rate:  # a new job comes
            nw_len_seq[i], nw_size_seq[i, :] = nw_dist()

    nw_len_seq = np.reshape(nw_len_seq,
                            [pa.num_ex, pa.simu_len])
    nw_size_seq = np.reshape(nw_size_seq,
                             [pa.num_ex, pa.simu_len, pa.num_res])

    return nw_len_seq, nw_size_seq
