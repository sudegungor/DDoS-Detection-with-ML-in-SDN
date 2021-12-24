import subprocess
import re
import io

class Terminal:

    @staticmethod
    def run(cmd:list):
        p = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            )
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                return Terminal._list_to_dict(Terminal._output_to_list(line))
        p.wait()



    @staticmethod
    def _output_to_list(input_string):
        return re.split("\\s+", str(input_string))

    @staticmethod
    def _list_to_dict(liste: list):
            try:
                return {
                'protocol_type': str(liste[4]).lower(),
                'source_ip': liste[2],
                'destination_ip': liste[3],
                'duration': liste[1]
                }
            except:
                print('veriler düzgün okunamadı')
