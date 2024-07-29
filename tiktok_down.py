import pyktok as pyk


def download():
    user_in = input('Enter your tiktok link:')
    pyk.save_tiktok(user_in, True)
