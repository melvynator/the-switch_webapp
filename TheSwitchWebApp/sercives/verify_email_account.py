import json
import TheSwitchWebApp
from TheSwitchWebApp.lib.SecureMessage import SecureMessage
import sendgrid
import os, config
from sendgrid.helpers.mail import *
from flask import url_for


def verify_email_account(first_name, last_name, email):
    register_account = {"first_name": first_name, "last_name": last_name, "email": email}
    register_account_json = json.dumps(register_account)
    encrypted_token = SecureMessage().encrypt(register_account_json)
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    mail = build_registration_email(register_account["first_name"], encrypted_token)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response


def build_registration_email(user, token):
    from_email = Email("switch-no-reply@gmail.com")
    to_email = Email("peignonmel@eisti.eu")
    subject = "Welcome to the Switch! Confirm your account"
    print(url_for("register.display_register_form", token=token.decode("utf-8")))
    content = Content("text/html", verification_email.format(user, url_for("register.display_register_form",
                                                                           token=token.decode("utf-8"),
                                                                           _external=True)))
    mail = Mail(from_email, subject, to_email, content)
    return mail


verification_email = """\
 <head>
  <title>The Switch</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <style>
  </style>
</head>

<body style="max-width:532px;margin:0 auto;padding:0;" dir="ltr" bgcolor="#ffffff">
  <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
    <tbody>
      <tr>
        <td width="100%" align="center" style="">
          <table border="0" cellspacing="0" cellpadding="0" align="center" style="border-collapse:collapse;">
            <tbody>
              <tr>
                <td width="1064" align="center" style="">
                  <table border="0" cellspacing="0" cellpadding="0" align="center" id="email_table" style="border-collapse:collapse;max-width:532px;margin:0 auto;">
                    <tbody>
                      <tr>
                        <td id="email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff;">
                          <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                            <tbody>
                              <tr>
                                <td height="1" colspan="5" style="line-height:1px;"><span style="color:#FFFFFF;display:none !important;font-size:1px;">&nbsp; You're almost ready to get started with The Switch. Please confirm your email, to define your paswword and so we know it's really you. &nbsp; What's The Switch? &nbsp; The switch is an application that will automatically send to your relatives documents that you will have created in case you are incapacitated. The incapacitation is defined if you are not able to click on a link that will be sent to you. &nbsp; https://fb.me/2cwhrJgLqOpqphH &nbsp;</span></td>
                              </tr>
                              <tr>
                                <td colspan="5" style="">
                                  <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                                    <tbody>
                                      <tr style="">
                                        <td height="8" style="line-height:8px;">&nbsp;</td>
                                      </tr>
                                      <tr>
                                        <td width="16" style="display:block;width:16px;">&nbsp;&nbsp;&nbsp;</td>
                                        <td width="24" align="left" valign="middle" colspan="1" style="height:24;line-height:0px;"><img src="https://static.xx.fbcdn.net/rsrc.php/v3/yy/r/QviS9ZDMP-M.png" width="24" height="24" style="border:0;"></td>
                                        <td colspan="1" style="padding-left:8px;"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:14px;line-height:20px;color:#373a43;">The Switch</span></td>
                                      </tr>
                                      <tr style="">
                                        <td height="8" style="line-height:8px;">&nbsp;</td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                              <tr>
                                <td colspan="5" style="">
                                  <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;background-color:#083064;background-size:100%;">
                                    <tbody>
                                      <tr>
                                        <td style=""></td>
                                        <td style="">
                                          <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;background-color:#083064;background-size:100%;">
                                            <tbody>
                                              <tr style="">
                                                <td height="32" style="line-height:32px;" colspan="3">&nbsp;</td>
                                              </tr>
                                              <tr>
                                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                                                <td width="20" style="display:block;width:20px;" class="mb_hide">&nbsp;&nbsp;&nbsp;</td>
                                                <td align="center" style="">
                                                  <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;">
                                                    <tbody>
                                                      <tr>
                                                        <td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-bottom:10px;">
                                                          <center><span class="mb_work_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:20px;line-height:24px;font-weight:normal;color:#FFFFFF;letter-spacing:0.2px;text-shadow:1px 1px 2px rgba(0,0,0,0.19);">Hi {0}! <br> Start using The Switch and add relatives to share sensitives information.</span></center>
                                                        </td>
                                                      </tr>
                                                      <tr>
                                                        <td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-top:10px;">
                                                          <center>
                                                            <a href="#"
                                                              style="color:#3b5998;text-decoration:none;" target="_blank">
                                                              <table border="0" width="200px" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                                                                <tbody>
                                                                  <tr>
                                                                    <td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border-radius:4px;box-shadow:0 1px 6px rgba(0, 0, 0, 0.08);background:#42B72A;margin:0px 0px 0px 0px;padding:4px 0px 4px 0px;padding:14px 16px 14px 16px;"><a href="{1}"
                                                                        style="color:#3b5998;text-decoration:none;" target="_blank"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;color:#ffffff;font-size:16px;line-height:18px;font-weight:500;">Confirm&nbsp;Email</span></a></td>
                                                                  </tr>
                                                                </tbody>
                                                              </table>
                                                            </a>
                                                          </center>
                                                        </td>
                                                      </tr>
                                                    </tbody>
                                                  </table>
                                                </td>
                                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                                                <td width="20" style="display:block;width:20px;" class="mb_hide">&nbsp;&nbsp;&nbsp;</td>
                                              </tr>
                                              <tr style="">
                                                <td height="24" style="line-height:24px;" colspan="3">&nbsp;</td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                        <td style=""></td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                              <tr style="">
                                <td height="4" style="line-height:4px;" colspan="3">&nbsp;</td>
                              </tr>
                              <tr class="mb_hide" style="">
                                <td height="4" style="line-height:4px;" colspan="3">&nbsp;</td>
                              </tr>
                              <tr style="align:center;">
                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                                <td width="16" style="display:block;width:16px;">&nbsp;&nbsp;&nbsp;</td>
                                <td style="">
                                  <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;">
                                    <tbody>
                                      <tr>
                                        <td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding:0px 0px 0px 0px;background-color:#ffffff;border-left:1px solid #ccc;border-right:1px solid #ccc;border-top:1px solid #ccc;border-bottom:1px solid #ccc;border-radius:0px;border:0px;">
                                          <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                                            <tbody>
                                              <tr style="">
                                                <td height="28" style="line-height:28px;">&nbsp;</td>
                                              </tr>
                                              <tr>
                                                <td style="">
                                                  <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                                                    <tbody>
                                                      <tr>
                                                        <td align="center" style="">
                                                          <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;">
                                                            <tbody>
                                                              <tr>
                                                                <td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-bottom:12px;">
                                                                  <table border="0" cellspacing="0" cellpadding="0" align="center" style="border-collapse:collapse;">
                                                                    <tbody>
                                                                      <tr>
                                                                        <td align="center" style=""><span class="mb_work_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:20px;color:#3D4452;letter-spacing:0.2px;">You're almost ready to get started with The Switch. Please confirm your email, to define your password and so we know it's really you.</span></td>
                                                                      </tr>
                                                                    </tbody>
                                                                  </table>
                                                                </td>
                                                              </tr>
                                                              <tr>
                                                                <td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding-top:12px;padding-bottom:12px;">
                                                                  <table border="0" cellspacing="0" cellpadding="0" align="center" style="border-collapse:collapse;">
                                                                    <tbody>
                                                                      <tr style="border-top:solid 1px #e5e5e5;">
                                                                        <td height="24" style="line-height:24px;">&nbsp;</td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td align="center" style="text-transform:uppercase;"><span class="mb_work_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:12px;line-height:20px;color:#4b4f56;letter-spacing:0.2px;"><b>What's The Switch?</b></span></td>
                                                                      </tr>
                                                                      <tr style="">
                                                                        <td height="8" style="line-height:8px;">&nbsp;</td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td align="center" style=""><span class="mb_work_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:20px;color:#90949c;">The switch is an application that will automatically send to your relatives documents that you will have created in case you are incapacitated. The incapacitation is defined if you are not able to click on a link that will be sent to you.</span></td>
                                                                      </tr>
                                                                    </tbody>
                                                                  </table>
                                                                </td>
                                                              </tr>
                                                            </tbody>
                                                          </table>
                                                        </td>
                                                      </tr>
                                                    </tbody>
                                                  </table>
                                                </td>
                                              </tr>
                                              <tr style="">
                                                <td height="14" style="line-height:14px;">&nbsp;</td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                                <td width="16" style="display:block;width:16px;">&nbsp;&nbsp;&nbsp;</td>
                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                              </tr>
                              <tr style="">
                                <td height="10" style="line-height:10px;" colspan="3">&nbsp;</td>
                              </tr>
                              <!--
                              <tr>
                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                                <td width="16" style="display:block;width:16px;">&nbsp;&nbsp;&nbsp;</td>
                                <td style="padding:10px 0px 0px 0px;">
                                  <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
                                    <tbody>
                                      <tr>
                                        <td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:12px;color:#A2A8B2;border-top:solid 1px #D8D8D8;line-height:14px;background:#FFFFFF;padding:10px 0px 0px 0px;text-align:left;">This message was sent to <a href="mailto:" style="color:#3b5998;text-decoration:none;" target="_blank">hello@SmilesDavis.yeah</a>. If you don't want to receive these emails from Workplace
                                          in the future, please <a href="#" style="color:#3b5998;text-decoration:none;"
                                            target="_blank">unsubscribe</a>.<br>Facebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025</td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                                <td width="16" style="display:block;width:16px;">&nbsp;&nbsp;&nbsp;</td>
                                <td width="8" style="display:block;width:8px;">&nbsp;&nbsp;&nbsp;</td>
                              </tr>
                              -->
                              <tr style="">
                                <td height="20" style="line-height:20px;" colspan="3">&nbsp;</td>
                              </tr>
                            </tbody>
                          </table><span style=""><img src="https://www.facebook.com/email_open_log_pic.php?mid=HMjU3NjA5MDM2Om1hdHRAcmVhbGx5Z29vZGVtYWlscy5jb206MTY2OA" style="border:0;width:1px;height:1px;"></span></td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>


</body>"""