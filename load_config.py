from netmiko import ConnectHandler
import yaml

def connect(port_number):
    ssh_connect = ConnectHandler(
        device_type="cisco_ios_telnet",
        ip="95.59.174.106",
        username="",
        password="",
        port=port_number)

    return ssh_connect

def load_config(ssh_connect, config_file):
    ssh_connect.send_config_from_file(config_file)

def main():
    path_to_config = "C:/Users/UlanAuyelbekov/Desktop/info/ccie/ine.ccie.rsv5.workbook.initial.configs/advanced.technology.labs/initial.ospf/"
    with open("devices.yaml") as dev:
        f = yaml.load(dev, Loader=yaml.FullLoader)
        for hostname, port_number in f.items():
            ssh_connect = ConnectHandler(port_number)
            load_config(ssh_connect, "{}{}.txt".format(path_to_config, str(hostname)))
            print(str(hostname) + " done")

if __name__ == "__main__":
    main()