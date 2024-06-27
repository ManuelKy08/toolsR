import requests

# Banner ASCII
banner = """
 /$$   /$$           /$$                 /$$               /$$$$$$                     
| $$  /$$/          | $$                | $$              /$$__  $$                    
| $$ /$$/   /$$$$$$ | $$   /$$  /$$$$$$ | $$   /$$       | $$  \__/  /$$$$$$   /$$$$$$$
| $$$$$/   /$$__  $$| $$  /$$/ /$$__  $$| $$  /$$//$$$$$$|  $$$$$$  /$$__  $$ /$$_____/
| $$  $$  | $$  \ $$| $$$$$$/ | $$  \ $$| $$$$$$/|______/ \____  $$| $$$$$$$$| $$      
| $$\  $$ | $$  | $$| $$_  $$ | $$  | $$| $$_  $$         /$$  \ $$| $$_____/| $$      
| $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$ \  $$       |  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/  \__/ \______/ |__/  \__/ \______/ |__/  \__/        \______/  \_______/ \_______/
                                                                        
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================
"""

print(banner)

# Daftar jalur admin yang umum digunakan
admin_paths = [
    'admin/', 'administrator/', 'login.php', 'administration/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/',
    'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/',
    'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp',
    'admin/login.asp', 'admin/admin.asp', '/login.aspx', 'admin_area/admin.asp', 'admin_area/login.asp',
    'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/admin.html',
    'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp', 'bb-admin/index.asp', 'bb-admin/login.asp',
    'bb-admin/admin.asp', 'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html',
    'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'administrator/index.html', 'administrator/login.html',
    'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator.html',
    'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html', 'admincontrol.html', 'admin_login.html',
    'panel-administracion/login.html', 'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp',
    'admin/admin-login.asp', 'admin-login.asp', 'admin/cp.asp', 'cp.asp', 'administrator/account.asp', 'administrator.asp',
    'acceso.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp', 'moderator/login.asp', 'administrator/login.asp',
    'moderator/admin.asp', 'controlpanel.asp', 'admin/account.html', 'adminpanel.html', 'webadmin.html', 'administration',
    'pages/admin/admin-login.html', 'admin/admin-login.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html',
    'user.asp', 'user.html', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/adminLogin.html',
    'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'adminarea/index.html', 'adminarea/admin.html', 'adminarea/login.html',
    'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
    'admin/admin_login.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'admin/account.asp',
    'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp', 'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp',
    'admin_login.asp', 'panel-administracion/login.asp', 'adminLogin.asp', 'admin/adminLogin.asp', 'home.asp', 'admin.asp',
    'adminarea/index.asp', 'adminarea/admin.asp', 'adminarea/login.asp', 'admin-login.html', 'panel-administracion/index.asp',
    'panel-administracion/admin.asp', 'modelsearch/index.asp', 'modelsearch/admin.asp', 'administrator/index.asp',
    'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp', 'admin2/index.asp',
    'adm/index.asp', 'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp',
    'siteadmin/index.asp', 'siteadmin/login.html', 'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php',
    'admin/login.php', 'admin/admin.php', 'admin/account.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php',
    'siteadmin/index.php', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
    'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php', 'admin_area/login.html',
    'admin_area/index.html', 'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
    'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html',
    'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.php', 'cp.php', 'administrator/index.php',
    'administrator/login.php', 'nsw/admin/login.php', 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
    'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php', 'admin/admin-login.php',
    'admin-login.php', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html', 'login.php',
    'modelsearch/login.php', 'moderator.php', 'moderator/login.php', 'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html',
    'admin/admin-login.html', 'admin-login.html', 'controlpanel.php', 'admincontrol.php', 'admin/adminLogin.html', 'adminLogin.html',
    'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.php',
    'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.php',
    'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html',
    'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
    'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html',
    'moderator/admin.html', 'user.php', 'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.php', 'wp-login.php',
    'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'admin.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php',
    'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php',
    'adm/admloginuser.php', 'admloginuser.php', 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php', 'adm/index.php', 'adm.php',
    'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php', 'adm/', 'admin/account.cfm', 'admin/index.cfm', 'admin/login.cfm',
    'admin/admin.cfm', 'admin/account.cfm', 'admin_area/admin.cfm', 'admin_area/login.cfm', 'siteadmin/login.cfm', 'siteadmin/index.cfm', 'siteadmin/login.html',
    'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/index.cfm', 'bb-admin/index.cfm', 'bb-admin/login.cfm',
    'bb-admin/admin.cfm', 'admin/home.cfm', 'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.cfm', 'admin.cfm', 'admincp/index.asp',
    'admincp/login.asp', 'admincp/index.html', 'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html',
    'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.cfm', 'cp.cfm', 'administrator/index.cfm',
    'administrator/login.cfm', 'nsw/admin/login.cfm', 'webadmin/login.cfm', 'admin/admin_login.cfm', 'admin_login.cfm', 'administrator/account.cfm',
    'administrator.cfm', 'admin_area/admin.html', 'pages/admin/admin-login.cfm', 'admin/admin-login.cfm', 'admin-login.cfm', 'bb-admin/index.html',
    'bb-admin/login.html', 'acceso.cfm', 'bb-admin/admin.html', 'admin/home.html', 'login.cfm', 'modelsearch/login.cfm', 'moderator.cfm',
    'moderator/login.cfm', 'moderator/admin.cfm', 'account.cfm', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html',
    'controlpanel.cfm', 'admincontrol.cfm', 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.cfm',
    'adminarea/index.html', 'adminarea/admin.html', 'webadmin.cfm', 'webadmin/index.cfm', 'webadmin/admin.cfm', 'admin/controlpanel.html', 'admin.html',
    'admin/cp.html', 'cp.html', 'adminpanel.cfm', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html',
    'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html',
    'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
    'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.cfm', 'account.html', 'controlpanel.html',
    'admincontrol.html', 'panel-administracion/login.cfm', 'wp-login.cfm', 'adminLogin.cfm', 'admin/adminLogin.cfm', 'home.cfm', 'admin.cfm',
    'adminarea/index.cfm', 'adminarea/admin.cfm', 'adminarea/login.cfm', 'panel-administracion/index.cfm', 'panel-administracion/admin.cfm',
    'modelsearch/index.cfm', 'modelsearch/admin.cfm', 'admincontrol/login.cfm', 'adm/admloginuser.cfm', 'admloginuser.cfm', 'admin2.cfm',
    'admin2/login.cfm', 'admin2/index.cfm', 'usuarios/login.cfm', 'adm/index.cfm', 'adm.cfm', 'affiliate.cfm', 'adm_auth.cfm', 'memberadmin.cfm',
    'administratorlogin.cfm', 'admin/account.pl', 'admin/index.pl', 'admin/login.pl', 'admin/admin.pl', 'admin/account.pl', 'admin_area/admin.pl',
    'admin_area/login.pl', 'siteadmin/login.pl', 'siteadmin/index.pl', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html',
    'admin/admin.html', 'admin_area/index.pl', 'bb-admin/index.pl', 'bb-admin/login.pl', 'bb-admin/admin.pl', 'admin/home.pl', 'admin_area/login.html',
    'admin_area/index.html', 'admin/controlpanel.pl', 'admin.pl', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/account.html',
    'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html',
    'panel-administracion/login.html', 'admin/cp.pl', 'cp.pl', 'administrator/index.pl', 'administrator/login.pl', 'nsw/admin/login.pl', 'webadmin/login.pl',
    'admin/admin_login.pl', 'admin_login.pl', 'administrator/account.pl', 'administrator.pl', 'admin_area/admin.html', 'pages/admin/admin-login.pl',
    'admin/admin-login.pl', 'admin-login.pl', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.pl', 'bb-admin/admin.html', 'admin/home.html',
    'login.pl', 'modelsearch/login.pl', 'moderator.pl', 'moderator/login.pl', 'moderator/admin.pl', 'account.pl', 'pages/admin/admin-login.html',
    'admin/admin-login.html', 'admin-login.html', 'controlpanel.pl', 'admincontrol.pl', 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html',
    'home.html', 'rcjakar/admin/login.pl', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.pl', 'webadmin/index.pl', 'webadmin/admin.pl',
    'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.pl', 'moderator.html', 'administrator/index.html',
    'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html',
    'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html',
    'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.pl', 'account.html',
    'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.pl', 'wp-login.pl', 'adminLogin.pl', 'admin/adminLogin.pl', 'home.pl',
    'admin.pl', 'adminarea/index.pl', 'adminarea/admin.pl', 'adminarea/login.pl', 'panel-administracion/index.pl', 'panel-administracion/admin.pl',
    'modelsearch/index.pl', 'modelsearch/admin.pl', 'admincontrol/login.pl', 'adm/admloginuser.pl', 'admloginuser.pl', 'admin2.pl', 'admin2/login.pl',
    'admin2/index.pl', 'usuarios/login.pl', 'adm/index.pl', 'adm.pl', 'affiliate.pl', 'adm_auth.pl', 'memberadmin.pl', 'administratorlogin.pl',
    'admin/account.py', 'admin/index.py', 'admin/login.py', 'admin/admin.py', 'admin/account.py', 'admin_area/admin.py', 'admin_area/login.py',
    'siteadmin/login.py', 'siteadmin/index.py', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html',
    'admin/admin.html', 'admin_area/index.py', 'bb-admin/index.py', 'bb-admin/login.py', 'bb-admin/admin.py', 'admin/home.py',
    'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.py', 'admin.py', 'admincp/index.asp', 'admincp/login.asp',
    'admincp/index.html', 'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html',
    'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.py', 'cp.py',
    'administrator/index.py', 'administrator/login.py', 'nsw/admin/login.py', 'webadmin/login.py', 'admin/admin_login.py', 'admin_login.py',
    'administrator/account.py', 'administrator.py', 'admin_area/admin.html', 'pages/admin/admin-login.py', 'admin/admin-login.py', 'admin-login.py',
    'bb-admin/index.html', 'bb-admin/login.html', 'acceso.py', 'bb-admin/admin.html', 'admin/home.html', 'login.py', 'modelsearch/login.py',
    'moderator.py', 'moderator/login.py', 'moderator/admin.py', 'account.py', 'pages/admin/admin-login.html', 'admin/admin-login.html',
    'admin-login.html', 'controlpanel.py', 'admincontrol.py', 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
    'rcjakar/admin/login.py', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.py', 'webadmin/index.py', 'webadmin/admin.py',
    'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.py', 'moderator.html', 'administrator/index.html',
    'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html',
    'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html',
    'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.py', 'account.html',
    'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.py', 'wp-login.py', 'adminLogin.py', 'admin/adminLogin.py', 'home.py',
    'admin.py', 'adminarea/index.py', 'adminarea/admin.py', 'adminarea/login.py', 'panel-administracion/index.py', 'panel-administracion/admin.py',
    'modelsearch/index.py', 'modelsearch/admin.py', 'admincontrol/login.py', 'adm/admloginuser.py', 'admloginuser.py', 'admin2.py',
    'admin2/login.py', 'admin2/index.py', 'usuarios/login.py', 'adm/index.py', 'adm.py', 'affiliate.py', 'adm_auth.py', 'memberadmin.py',
    'administratorlogin.py', 'admin/account.rb', 'admin/index.rb', 'admin/login.rb', 'admin/admin.rb', 'admin/account.rb', 'admin_area/admin.rb',
    'admin_area/login.rb', 'siteadmin/login.rb', 'siteadmin/index.rb', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html',
    'admin/login.html', 'admin/admin.html', 'admin_area/index.rb', 'bb-admin/index.rb', 'bb-admin/login.rb', 'bb-admin/admin.rb', 'admin/home.rb',
    'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.rb', 'admin.rb', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
    'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html',
    'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.rb', 'cp.rb', 'administrator/index.rb',
    'administrator/login.rb', 'nsw/admin/login.rb', 'webadmin/login.rb', 'admin/admin_login.rb', 'admin_login.rb', 'administrator/account.rb',
    'administrator.rb', 'admin_area/admin.html', 'pages/admin/admin-login.rb', 'admin/admin-login.rb', 'admin-login.rb', 'bb-admin/index.html',
    'bb-admin/login.html', 'acceso.rb', 'bb-admin/admin.html', 'admin/home.html', 'login.rb', 'modelsearch/login.rb', 'moderator.rb',
    'moderator/login.rb', 'moderator/admin.rb', 'account.rb', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html',
    'controlpanel.rb', 'admincontrol.rb', 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.rb',
    'adminarea/index.html', 'adminarea/admin.html', 'webadmin.rb', 'webadmin/index.rb', 'webadmin/admin.rb', 'admin/controlpanel.html', 'admin.html',
    'admin/cp.html', 'cp.html', 'adminpanel.rb', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html',
    'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html',
    'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html',
    'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.rb', 'account.html', 'controlpanel.html', 'admincontrol.html',
    'panel-administracion/login.rb', 'wp-login.rb', 'adminLogin.rb', 'admin/adminLogin.rb', 'home.rb', 'admin.rb', 'adminarea/index.rb',
    'adminarea/admin.rb', 'adminarea/login.rb', 'panel-administracion/index.rb', 'panel-administracion/admin.rb', 'modelsearch/index.rb',
    'modelsearch/admin.rb', 'admincontrol/login.rb', 'adm/admloginuser.rb', 'admloginuser.rb', 'admin2.rb', 'admin2/login.rb', 'admin2/index.rb',
    'usuarios/login.rb', 'adm/index.rb', 'adm.rb', 'affiliate.rb', 'adm_auth.rb', 'memberadmin.rb', 'administratorlogin.rb', 'admin/account.xml',
    'admin/index.xml', 'admin/login.xml', 'admin/admin.xml', 'admin/account.xml', 'admin_area/admin.xml', 'admin_area/login.xml', 'siteadmin/login.xml',
    'siteadmin/index.xml', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
    'admin_area/index.xml', 'bb-admin/index.xml', 'bb-admin/login.xml', 'bb-admin/admin.xml', 'admin/home.xml', 'admin_area/login.html',
    'admin_area/index.html', 'admin/controlpanel.xml', 'admin.xml', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/account.html',
    'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html',
    'panel-administracion/login.html', 'admin/cp.xml', 'cp.xml', 'administrator/index.xml', 'administrator/login.xml', 'nsw/admin/login.xml',
    'webadmin/login.xml', 'admin/admin_login.xml', 'admin_login.xml', 'administrator/account.xml', 'administrator.xml', 'admin_area/admin.html',
    'pages/admin/admin-login.xml', 'admin/admin-login.xml', 'admin-login.xml', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.xml',
    'bb-admin/admin.html', 'admin/home.html', 'login.xml', 'modelsearch/login.xml', 'moderator.xml', 'moderator/login.xml', 'moderator/admin.xml',
    'account.xml', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html', 'controlpanel.xml', 'admincontrol.xml',
    'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.xml', 'adminarea/index.html',
    'adminarea/admin.html', 'webadmin.xml', 'webadmin/index.xml', 'webadmin/admin.xml', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html',
    'cp.html', 'adminpanel.xml', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
    'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
    'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html',
    'moderator/admin.html', 'user.xml', 'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.xml', 'wp-login.xml',
    'adminLogin.xml', 'admin/adminLogin.xml', 'home.xml', 'admin.xml', 'adminarea/index.xml', 'adminarea/admin.xml', 'adminarea/login.xml',
    'panel-administracion/index.xml', 'panel-administracion/admin.xml', 'modelsearch/index.xml', 'modelsearch/admin.xml', 'admincontrol/login.xml',
    'adm/admloginuser.xml', 'admloginuser.xml', 'admin2.xml', 'admin2/login.xml', 'admin2/index.xml', 'usuarios/login.xml', 'adm/index.xml',
    'adm.xml', 'affiliate.xml', 'adm_auth.xml', 'memberadmin.xml', 'administratorlogin.xml', 'admin/account.xhtml', 'admin/index.xhtml',
    'admin/login.xhtml', 'admin/admin.xhtml', 'admin/account.xhtml', 'admin_area/admin.xhtml', 'admin_area/login.xhtml', 'siteadmin/login.xhtml',
    'siteadmin/index.xhtml', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
    'admin_area/index.xhtml', 'bb-admin/index.xhtml', 'bb-admin/login.xhtml', 'bb-admin/admin.xhtml', 'admin/home.xhtml', 'admin_area/login.html',
    'admin_area/index.html', 'admin/controlpanel.xhtml', 'admin.xhtml', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
    'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html',
    'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.xhtml', 'cp.xhtml', 'administrator/index.xhtml',
    'administrator/login.xhtml', 'nsw/admin/login.xhtml', 'webadmin/login.xhtml', 'admin/admin_login.xhtml', 'admin_login.xhtml',
    'administrator/account.xhtml', 'administrator.xhtml', 'admin_area/admin.html', 'pages/admin/admin-login.xhtml', 'admin/admin-login.xhtml',
    'admin-login.xhtml', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.xhtml', 'bb-admin/admin.html', 'admin/home.html', 'login.xhtml',
    'modelsearch/login.xhtml', 'moderator.xhtml', 'moderator/login.xhtml', 'moderator/admin.xhtml', 'account.xhtml', 'pages/admin/admin-login.html',
    'admin/admin-login.html', 'admin-login.html', 'controlpanel.xhtml', 'admincontrol.xhtml', 'admin/adminLogin.html', 'adminLogin.html',
    'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.xhtml', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.xhtml',
    'webadmin/index.xhtml', 'webadmin/admin.xhtml', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.xhtml',
    'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html'
]

# Meminta input URL target dari pengguna
target_url = input("Enter the target URL (e.g., https://example.com): ").strip()

# Memastikan URL memiliki skema
if not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "http://" + target_url

print(f"Scanning {target_url} for admin login pages...\n")

# Fungsi untuk memeriksa apakah halaman admin ada
def check_admin_path(url, paths):
    for path in paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Found admin login page: {full_url}")
            else:
                print(f"Checked: {full_url} (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"Failed to access {full_url}: {e}")

# Memanggil fungsi untuk memeriksa halaman admin
check_admin_path(target_url, admin_paths)

print("\nScan complete.")
