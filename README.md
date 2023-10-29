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
`deviceSN` is a list of serial numbers. In this example, we only test with a single device.

The FortiZTP API returns the HTTP response "204 No Content" on success.

**Code**
```
update = fortiztp.devices.update(
    deviceSN = ["FGT60FTK1234ABCD"],
    deviceType = "FortiGate",
    provisionStatus = "provisioned",
    provisionTarget = "FortiManager"
)
print(update)
```

**Output**
```
204
```

> **Note:** You cannot provision the same device twice. You need to unprovision it first, before provisioning it again.

### Unprovision a device from FortiManager.
`deviceSN` is a list of serial numbers. In this example, we only test with a single device.

The FortiZTP API returns the HTTP response "204 No Content" on success.

**Code**
```
update = fortiztp.devices.update(
    deviceSN = ["FGT60FTK1234ABCD"],
    deviceType = "FortiGate",
    provisionStatus = "unprovisioned",
    provisionTarget = "FortiManager"
)
print(update)
```

**Output**
```
204
```

### Error messages.
Error messages are provided as is, from the FortiZTP API.

**Code**
```
update = fortiztp.devices.update(
    deviceSN = ["FGT60FTK1234ABCD", "testSN"],
    deviceType = "FortiGate",
    provisionStatus = "provisioned",
    provisionTarget = "FortiManager"
)
print(update)
```

**Output**
```
{
    "error": "invalid_request",
    "error_description": "Device testSN doesn't exist in this account"
}
```