def find_email(linkedin_url):

    username = linkedin_url.split("/")[-1]

    return f"{username}@company.com"