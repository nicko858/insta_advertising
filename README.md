# Instagram advertising

This script created for automatic [instagram](https://www.instagram.com/) promotion.
It helps you to get winners of your promotion Instagram post.

The script uses [Instabot](https://github.com/instagrambot/instabot) as interface to Instagram API.

If everything is fine, you'll see a list with promotion winners.

### How to install
Python3 should be already installed.
```bash
$ git clone https://github.com/nicko858/insta_advertising.git
$ cd insta_advertising
$ pip install -r requirements.txt
```

- Create account on the [instagram](https://www.instagram.com/), or use existing
- Create your promotion post, or use existing. Remember it's url
- Create file `.env` in the script directory
- Add the following records to the `.env-file`:  

   ```bash
   INST_LOGIN=<your_Instagram_login>
   INST_PASSWD=<your_Instagram_passwd>
  ```
  
### How to run
The script required command line arguments:

```bash
python instagram_promotion.py <promo_owner> <post_url>
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
