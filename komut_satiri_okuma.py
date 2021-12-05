import re
input_string = '27 11.264063351     10.0.0.1 → 10.0.0.3     ICMP 98 Echo (ping) request  id=0x10c5, seq=15/3840, ttl=64'
# input_string = 'kaan kizildag    asfafa'

listem = re.split("\\s+", input_string)


def list_to_dict(liste: list):
    return {
        'protocol_type': liste[5],
        'source_ip': liste[2],
        'destination_ip': liste[4],
        'duration': liste[1]
    }


print(list_to_dict(listem))
