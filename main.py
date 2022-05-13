from Date import Date_
from ShopifyApp import Shopify
from mail import SendEmail
def main():
    shopify=Shopify()
    # from datetime import date
    date_=Date_("May 2, 2022 at 10:08 pm")
    date_.convert_date_in_numbers()
    print(date_.match_date())
    shopify.open_login_window()
    shopify.login()
    list_activity=shopify.open_workplace()
    installation_mail="<p>Hello there,</p><p>Welcome to Picamaze!</p><p>My name is Garima Dhebana</p><br><p>I&rsquo;m thrilled to have you as a part of the Picamaze team. Are you ready to set up? If you are curious about Picamaze or have any queries, We've got your back. You can reply to this email and I&rsquo;ll be happy to be of your service.</p><p>&nbsp;</p><p>Happy selling!</p><p>&nbsp;</p><p>Regards,</p><p>Garima Dhebana</p><p>Customer Success Manager</p><p>Propero Consulting Pvt. Ltd.</p>"
    uninstallation_mail='<p dir="ltr">Hello there,</p><p dir="ltr">My name is Garima from Picamaze.</p><p dir="ltr">We&rsquo;re really sorry to see you go. Too bad it didn&rsquo;t work out, but no hard feelings, right? We still care about you.&nbsp;</p><p dir="ltr">If you have got a few seconds please reply to this email with the reason why you have uninstalled it. Would love to know how we can do a better job.</p><p dir="ltr">Happy selling!</p><p dir="ltr"><a href="https://apps.shopify.com/picamaze">https://apps.shopify.com/picamaze</a>&nbsp;</p><p dir="ltr">Regards,</p><p dir="ltr">Garima Dhebana&nbsp;</p><p dir="ltr">Customer Success Manager</p><p dir="ltr">Propero Consulting Pvt. Ltd.</p>'
    cancel_recurring_charge='<p dir="ltr">Hello there,</p><p dir="ltr">My name is Garima from Picamaze.</p><p dir="ltr">I noticed you canceled recurring charges for Picamaze, but no hard feelings.</p><p dir="ltr">Please help us learn more about why you have decided to cancel your charges. Did you expect something which was not there?</p><p dir="ltr">If you have got a few seconds please reply to this email with the reason why you have canceled it. Would love to know how we can do a better job.</p><p dir="ltr">Happy selling!</p><p dir="ltr">Regards,</p><p dir="ltr">Garima Dhebana&nbsp;</p><p dir="ltr">Customer Success Manager</p><p dir="ltr">Propero Consulting Pvt. Ltd.</p>'
    #'<p>Hello there,</p><p>Welcome to Picamaze!</p><p>My name is Garima Dhebana</p>'
    #'lokendra@propero.in'
    for mail_to in list_activity['Installed']:
        print(mail_to)
        #mail=SendEmail(mail_for_install)
        #mail=SendEmail('garima.dhebana@propero.in')
        mail=SendEmail('lokendra@propero.in')
        #mail=SendEmail('vaishrishika@gmail.com')
        subject="Thank you for joining our club"
        # image_scrap=ImageScrapper()
        # url="https://stocksnap.io/search/"
        # search_query=input("Enter query:- ")
        # url=url+search_query
        # file=image_scrap.fetch_image(url)
        file=None
        msg=mail.create_msg(file,installation_mail,subject)
        mail.send_mail(msg)

if __name__=="__main__":
    main()
