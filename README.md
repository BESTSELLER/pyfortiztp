# pyfortiztp
Python API client library for Fortinet's [FortiZTP](https://fortiztp.forticloud.com).

The FortiZTP Cloud API provides:
 - Retrieve provisioning status of FortiGates, FortiAPs, and FortiSwitch.
 - Provision or un-provision devices to the cloud or on-premise targets.

## Installation
To install run `pip install pyfortiztp`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start
To begin, import pyfortiztp and instantiate the API.

We need to provide our API credentials to our FortiCloud account.
Additionally, we need to provide the external IP and serial number of our FortiManager instance.

**Code**
```
fortiztp = pyfortiztp.api(
    forticloud_host = "https://customerapiauth.fortinet.com",
    forticloud_userid = "<your forticloud userid>",
    forticloud_password = "<your forticloud password>",
    fmg_external_ip = "<external IP of your fortimanager>",
    fmg_external_serial = "<serial number of your fortimanager>"
)
```

## Examples
### Retrieve a single devices.
**Code**
```
devices = fortiztp.devices.all(deviceSN="FGT60FTK1234ABCD")
print(devices)
```

**Output**
```
{
    "deviceSN": "FGT60FTK1234ABCD",
    "deviceType": "FortiGate",
    "provisionStatus": "unprovisioned",
    "provisionTarget": null,
    "region": "global,europe,JP,US",
    "externalControllerSn": null,
    "externalControllerIp": null,
    "platform": null
}
```

### Provision a device to FortiManager.
**Code**
```
provision = fortiztp.devices.update(
    deviceSN = "FGT60FTK1234ABCD",
    deviceType = "FortiGate",
    provisionStatus = "provisioned",
    provisionTarget = "FortiManager"
)
print(provision)
```

**Output**
```
204
```

> **Note:** The FortiZTP API returns the HTTP response "204 No Content" on success.

### Unprovision a device from FortiManager.
**Code**
```
unprovision = fortiztp.devices.update(
    deviceSN = "FGT60FTK1234ABCD",
    deviceType = "FortiGate",
    provisionStatus = "unprovisioned",
    provisionTarget = "FortiManager"
)
print(unprovision)
```

**Output**
```
204
```

> **Note:** The FortiZTP API returns the HTTP response "204 No Content" on success.