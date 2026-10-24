import os
import logging
from src.parser_utils import parse_json
from src.network_device import NetworkDevice

def main():
    logger = logging.getLogger(__name__)
    logger.info("Starting network device summary application.")

    # Load data files (falling back to empty lists if files don't exist yet)
    devices_data = parse_json("data/devices.json") if os.path.exists("data/devices.json") else []
    interfaces_data = parse_json("data/interfaces.json") if os.path.exists("data/interfaces.json") else []
    vlans_data = parse_json("data/vlans.json") if os.path.exists("data/vlans.json") else []

    # 1. Original Device Summaries
    for item in devices_data:
        hostname = item.get("hostname")
        ip = item.get("ip")
        dev_type = item.get("type")

        if hostname and ip and dev_type:
            device = NetworkDevice(hostname=hostname, ip=ip, type=dev_type)
            device.summarize()

    # 2. Interface Messages
    for interface in interfaces_data:
        name = interface.get("name")
        status = interface.get("status")
        if name and status:
            msg = f"Interface {name} is {status}"
            print(msg)
            logger.info(f"INTERFACE_MSG: {msg}")

    # 3. Device Location/Role Messages
    for device in devices_data:
        hostname = device.get("hostname")
        location = device.get("location", "Unknown")
        role = device.get("role", "Unknown")
        if hostname:
            msg = f"Device {hostname} is a {location} {role}"
            print(msg)
            logger.info(f"DEVICE_MSG: {msg}")

    # 4. VLAN Messages
    for vlan in vlans_data:
        vlan_id = vlan.get("id")
        vlan_name = vlan.get("name")
        if vlan_id is not None and vlan_name:
            msg = f"VLAN {vlan_id} is the {vlan_name}"
            print(msg)
            logger.info(f"VLAN_MSG: {msg}")

if __name__ == "__main__":
    # Ensure logs directory exists and configure logging before start marker
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/lab.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    logger = logging.getLogger(__name__)
    
    # Log start marker
    logger.info("[LAB1-START]")
    
    # Run main program
    main()
    
    # Log end marker
    logger.info("[LAB1-END]")