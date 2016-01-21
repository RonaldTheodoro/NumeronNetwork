import os


class VNC(object):

    """Efetua o acesso via VNC"""

    def VNCAccess(self, ip, terminal):
        os.system('start PRO\\UltraVNC\\vncviewer.exe -connect {}:{}'.format(
            ip, terminal))
