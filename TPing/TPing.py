import os


class TPing(object):

    """Recebe um ip e efetua o teste de ping"""

    def TestPing(self, ip):
        os.system('start cmd /c ping {} -t'.format(ip))
