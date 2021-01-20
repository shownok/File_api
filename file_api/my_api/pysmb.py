from smb.SMBConnection import SMBConnection

conn = SMBConnection(userID='smb', password='123', client_machine_name='Akramul-PC', server_name='myserver',  use_ntlm_v2 = True)
server_ip='192.168.0.103',
assert conn.connect(server_ip, 139)