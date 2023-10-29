from pyfortiztp.models.devices import Devices


class Api(object):
    """Base API class.
    """

    def __init__(self, forticloud_userid: str, forticloud_password: str, fmg_external_ip: str, fmg_external_serial: str, fortiztp_host: str="https://fortiztp.forticloud.com", forticloud_host: str="https://customerapiauth.fortinet.com", client_id: str="fortiztp", verify: bool=True, **kwargs):
        self.forticloud_host = forticloud_host + "/api/v1"
        self.forticloud_userid = forticloud_userid
        self.forticloud_password = forticloud_password
        self.fmg_external_ip = fmg_external_ip
        self.fmg_external_serial = fmg_external_serial
        self.fortiztp_host = fortiztp_host + "/public/api/v1"
        self.client_id = client_id
        self.verify = verify
        self.access_token = None
        self.expires_in = None
        self.refresh_token = None
        self.timestamp = None

    @property
    def devices(self):
        """Endpoints related to device management.
        """
        return Devices(api=self)