print(CREATED BY ANESTUS UDUME, FROM BENTECH SECURITY)
import win32api
import win32con

# Set the username and password for the user to impersonate
username = 'user_to_impersonate'
password = 'user_password'

# Create a new thread and impersonate the user
thread_id, token_handle = win32api.LogonUser(
    username, None, password, win32con.LOGON32_LOGON_INTERACTIVE, win32con.LOGON32_PROVIDER_DEFAULT)
win32api.ImpersonateLoggedOnUser(token_handle)

# Perform actions as the impersonated user here

# Revert the impersonation
win32api.RevertToSelf()
