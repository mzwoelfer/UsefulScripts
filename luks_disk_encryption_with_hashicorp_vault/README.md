## Vaultlocker Alternative
Vaultlocker authenticates with [[Hashicorp Vault]] ot decrypt disks.
However it is not supported anymore and there might be a simpler way, instead of loading unnecessary python libraries. Simply doing it directly with systemd-files/calls.

MonkaS

🔗 URL: https://github.com/openstack-charmers/vaultlocker

# 0. 🔬Prerequisites
- RHEL based VM with an additional volume available
- Vault Server installed and configured
- auth method (userpass, approle, tls) avaibable
- KVv2 path enabled (e.g: luks/)
- vault policiy for KVv2 path access binded to the auth method

# 1. 🔐 Encrypt volume using luks
```bash
# install cryptsetup (luks)
...

# install vault rpm (https://developer.hashicorp.com/vault/downloads)
...

# find mounted device for volume
fdisk -l

# encrypt volume
´
cryptsetup -y -v --type luks luksFormat /dev/<device>
# -> enter passphrase

# TODO: write passphrase into vault
vault kv put luks/$(hostname -f) key=<PASSPHRASE>
```

# 2. ⚙️ create SystemD unit for luks volume decryption
```bash
# /usr/lib/systemd/system/luks.service
[Unit]
Description=luks
DefaultDependencies=no
After=networking.service
After=nss-lookup.target

[Service]
Type=oneshot
KillMode=none
Environment=VAULT_SKIP_VERIFY=true # optional
Environment=VAULT_ADDR=https://xxx.xxx.xxx.xxx:8200 # vault address
ExecStart=/bin/sh -c 'until (nc -z xxx.xxx.xxx.xxx 8200); do echo "wait for vault server"; done && VAULT_TOKEN=$(vault login -field=token -method=userpass username=luks password=luks) vault kv get -field=key luks/$(hostname -f) | cryptsetup luksOpen /dev/vdb vault -'
TimeoutSec=0

[Install]
WantedBy=multi-user.target
```

```bash
# reload systemd daemon
systemctl daemon-reload

# reboot
reboot
```

# 3. 🚀 Verify volume is encrypted at boot
```bash
# show volume status
cryptsetup -v status vault

# debug
journalctl -u luks -f
```

POGGERS