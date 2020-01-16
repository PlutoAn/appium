# -*- coding: utf-8 -*-

from common.basetask import *
from common import *

class androidSuiteTask(BaseTask):
    def initTask(self):
        tests = [a_guidance_001("guidance_001"),
                    a_guidance_002("guidance_002"),
                    a_guidance_003("guidance_003"),
                    a_guidance_004("guidance_004"),
                    a_guidance_005("guidance_005"),
                    a_guidance_006("guidance_006"),
                    a_guidance_007("guidance_007"),
                    a_guidance_008("guidance_008"),
                    a_guidance_009("guidance_009"),
                    a_guidance_010("guidance_010"),
                    a_guidance_011("guidance_011"),
                    a_guidance_012("guidance_012"),
                    a_download_001("download_001"),
                    a_download_002("download_002"),
                    a_download_003("download_003"),
                    a_download_006("download_006"),
                    a_download_007("download_007"),
                    a_download_008("download_008"),
                    a_download_009("download_009"),
                    a_download_010("download_010"),
                    a_download_018("download_018"),
                    a_download_022("download_022"),
                    a_download_023("download_023")]
                    
        # tests = [a_guidance_001("guidance_001")]
        
        self.setTask(tests)

    def initCommitCheckTask(self):
        tests = [a_commitCheck_001("commitCheck_001")]
        self.setTask(tests)