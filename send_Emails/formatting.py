msg_template="""Hello {name},
Thank you for joining with {website}. We are happy to have you with us.
"""

def format_msg(my_name='Abhishek',my_website="myWebsite.com"):
    my_msg=msg_template.format(name=my_name,website=my_website)
    return my_msg