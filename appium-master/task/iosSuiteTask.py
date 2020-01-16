# -*- coding: utf-8 -*- 

from common.basetask import *
from __init__ import *

class iosSuiteTask(BaseTask):
    def initTask(self):
        tests = [i_guidance_001("guidance_001"),
                    i_guidance_002("guidance_002"),
                    i_guidance_003("guidance_003"),
                    i_guidance_004("guidance_004"),
                    i_guidance_005("guidance_005"),
                    i_guidance_006("guidance_006"),
                    i_guidance_007("guidance_007"),
                    i_guidance_008("guidance_008"),
                    i_guidance_009("guidance_009"),
                    i_guidance_010("guidance_010"),
                    i_guidance_011("guidance_011"),
                    i_guidance_012("guidance_012"),
                    i_download_001("download_001"),
                    i_download_002("download_002"),
                    i_download_003("download_003"),
                    i_download_004("download_004"),
                    i_download_005("download_005"),
                    i_download_025("download_025"),
                    i_download_026("download_026"),
                    i_download_028("download_028")]
        self.setTask(tests)

    def initCommitCheckTask(self):
        tests = [i_commitCheck_001("commitCheck_001")]
        self.setTask(tests)