from pyfortiztp.core.fortiztp import FortiZTP
import requests


class Devices(FortiZTP):
    """API class for devices.
    """

    def __init__(self, **kwargs):
        super(Devices, self).__init__(**kwargs)

    def all(self, deviceSN: str=None):
        """Retrieves the status of a device.

        Args:
            deviceSN (str): Serial number of a specific device.
        """

        self.login()

        url = self.api.host + f"/devices"

        # Get a specific device
        if deviceSN:
            url += f"/{deviceSN}"

        response = requests.get(url, headers={'Authorization': 'Bearer ' + self.api.access_token}, verify=True)
        
        # HTTP 200 OK
        if response.status_code == 200:
            return response.json()

    def provision(self, deviceType: str, deviceSN: str, provisionStatus: str, provisionTarget: str, region: str=None, externalControllerIp: str=None, externalControllerSn: str=None):
        """Provisions or unprovisions a device.

        Args:
            deviceType (str): FortiGate, FortiAP, FortiSwitch or FortiExtender.
            deviceSN (str): Device serial number.
            provisionStatus (str): To provision device, set to 'provisioned'. To unprovision device, set to 'unprovisioned'.
            provisionTarget (str): FortiManager, FortiGateCloud, FortiLANCloud, FortiSwitchCloud, ExternalAC, FortiExtenderCloud.
            region (str): Only needed for FortiGateCloud, FortiLANCloud and FortiManagerCloud. For FortiLAN Cloud, please choose one available region for that device return from GET request. For FortiManager Cloud, region is the account region: US-WEST-1, EU-CENTRAL-1, CA-WEST-1 and AP-NORTHEAST-1 etc.
            externalControllerSn (str): Only needed for FortiManager provision.
            externalControllerIp (str): FQDN/IP. Needed for FortiManager or External AC provision.
        """

        self.login()

        if provisionTarget == "FortiGateCloud" or provisionTarget == "FortiManagerCloud" or provisionTarget == "FortiLANCoud":
            region = region

        if provisionTarget == "FortiManager" or provisionTarget == "ExternalAC":
            externalControllerIp = self.api.fmg_external_ip

        if provisionTarget == "FortiManager":
            externalControllerSn = self.api.fmg_external_serial

        data = {
            "deviceType": deviceType,
            "deviceSN": deviceSN,
            "provisionStatus": provisionStatus,
            "provisionTarget": provisionTarget,
            "region": region,
            "externalControllerIp": externalControllerIp,
            "externalControllerSn": externalControllerSn
        }

        response = requests.put(self.api.host + f"/devices/{deviceSN}/", headers={'Authorization': 'Bearer ' + self.api.access_token}, json=data, verify=True)

        # API returns 204 No Content on successful request        
        if response.status_code == 204:
            return response.status_code
        else:
            return response.json()