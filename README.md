## Description:

This is just a simple Discord bot that keeps track of new internships and job offerings on the UTCN website and posts the new entries on a Discord server.

I created this project to practice OOP principles with Python and to experiment on how Python as a programming language works.

## Technologies:
- Python
- Selenium
- Gecko webdriver
- CSV
- Discord bots

## Functionality:

- the bot uses Selenium and the Gecko webdriver to access the [UTCN webpage](https://www.utcluj.ro/ococ/oportunitati/) where the postings are located.
- after that it identifies the first 10 page elements that contain the postings information and begins to check each posting against a local CSV file in order to filter out any offer that was previously distributed on the Discord server
- these actions are also presented to the user in CLI:

  ![Screenshot from 2023-05-08 00-27-53](https://user-images.githubusercontent.com/38301587/236704422-44e1813e-1c58-4ddd-9ce7-830bf8109e2f.png)
  
- and finally in the last step the new postings are distributed to the Discord server:

![Screenshot from 2023-05-08 00-17-39](https://user-images.githubusercontent.com/38301587/236705210-ea2fa351-abc1-44da-bddd-5a821507f026.png)![Screenshot from 2023-05-08 00-17-24](https://user-images.githubusercontent.com/38301587/236705208-27c15190-df17-4558-84df-7f292f2a404e.png)
