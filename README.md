# 🚀 Siphub: Precision SIP-to-Social Media Gateway

Siphub is a professional bridge between **Asterisk PBX** and **Viber Desktop**. Route your SIP calls to the world for $0 using GUI automation.

### 📁 Configs Folder
You can find pre-configured Asterisk files of this repository.

### ❗ Vital Instructions for Stability
- **Windows Scaling:** Must be set to **100%**. Anything else will break the coordinates.
- **Window Management:** Viber Desktop must be the active window. Ensure no other apps overlap the coordinates.
- **Virtual Audio:** Use **VB-Audio Virtual Cable** to bridge **MicroSIP** and **Viber**.
- **VM Usage:** Fully compatible with VMware/VirtualBox as long as a virtual audio driver is present.

### ⚙️ How to Test
1. Set up your Asterisk using files in `/configs`.
2. Install **VB-Audio Cable** on your Windows Gateway.
3. Configure MicroSIP and Viber to use **Cable Output/Input**.
4. Run `gateway.py` as Administrator and dial!

**YOU NEED 1 LINUX VM (Asterisk) 1 WINDOWS VM (Viber + Python)**
**THE MOST WORKING SOLUTION %95 IS VMWARE**
**GIVE THEM A BRIDGE IP 192.168.1.XX**
