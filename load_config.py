from netmiko import ConnectHandler
import yaml

def connect():
    with open("ccie/devices.yaml") as dev:
        f = yaml.load(dev, Loader=yaml.FullLoader)
        a = list()
        for port_number in f.values():
            conn = {
                "device_type":"cisco_ios_telnet",
                "ip":"95.59.174.106",
                "username":"",
                "password":"",
                "port":port_number}

            a.append(conn)

    return a

def load_config(ssh_connect, config_file):
    ssh_connect.send_config_from_file(config_file)

def main():
    path_to_config = "C:/Users/UlanAuyelbekov/Desktop/info/ccie/ine.ccie.rsv5.workbook.initial.configs/advanced.technology.labs/initial.ospf/"
    a = connect()
    count = 1
    for i in range(len(a)):
        ssh_connect = ConnectHandler(**a[i])
        load_config(ssh_connect, "{}R{}.txt".format(path_to_config, str(count)))
        print("R{} ".format(count) + " done")
        count = count + 1

if __name__ == "__main__":
    main()