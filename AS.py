import json
import socket
import sys

def main():
	var_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(("127.0.0.1", 53533))
	with open("dns.json" , "w+") as f:
		while True:
			print("Running DNS Server on IP and port : 127.0.0.1 : 53533")
			msg, address = sock.recvfrom(512)
			msg_body = str(msg).split('\n')
			dns = json.loads("".join(f.readlines()))
			if len(msg_body) == 2:
				req_msg = {}
				for i in msg_body:
					p = i.split("=")
					if len(p) == 2:
						if p[0] == "TYPE" or p[0] =="NAME":
							req_msg[p[0]] = p[1]
						else:
							sock.sendall(b"false")
							continue
				dns_rec, pos = search_dns_list(dns,req_msg)
				if pos > -1:
					sock.sendall(b"TYPE=" + bytes(dns_rec.get("TYPE")) + b"\nNAME=" + bytes(dns_rec.get("NAME"))
                                 + b"\nVALUE=" + bytes(dns_rec.get("VALUE")) + b"\nTTL=" + bytes(
                        dns_rec.get("TTL")))
					continue
				else:
					sock.sendall(b"false")
			elif len(body) == 4:
				req_msg_2 = {}
				for i in msg_body:
					p2 = i.split("=")
					if len(p2) == 2:
						if p2[0] == "TYPE" or p2[0] == "NAME" or p2[0] == "VALUE" or p2[0] == "TTL":
							req_msg_2[p2[0]] = p[1]
						else:
							sock.sendall(b"false")
                            continue
                dns_rec, pos = find_in_dns_list(dns, req_msg)
                if pos > -1:
                    dns[pos] = req_msg_2
                else:
                    dns.push(req_msg_2)
                f.write(json.dumps(dns))
            sock.sendall(b"true")

def search_dns_list(dns_list, dns):
    i = 0
    for element in dns_list:
        i += 1
        if dns.get('TYPE') == element.get("TYPE") and dns.get("NAME") == element.get("NAME"):
            return element, i
    return [], -1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting Down DNS Server')
        sys.exit(0)
