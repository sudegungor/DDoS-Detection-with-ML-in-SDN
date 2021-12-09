import subprocess
import re


class Terminal:

    @staticmethod
    def run(cmd:list):
        output = subprocess.Popen(
            cmd, 
            shell = True, 
            stdout=subprocess.PIPE,
            bufsize=1
            ).communicate()[0]
        output.wait()
        res = re.findall(r'\'(.*?)\'', str(output))[0]

        # return Terminal._list_to_dict(
        #     Terminal._output_to_list(
        #         res
        #     )
        # )


    @staticmethod
    def _output_to_list(input_string):
        return re.split("\\s+", input_string)

    @staticmethod
    def _list_to_dict(liste: list):
        return {
            'protocol_type': liste[5],
            'source_ip': liste[2],
            'destination_ip': liste[4],
            'duration': liste[1]
        }
