from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://kick.com/shesjade"
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
