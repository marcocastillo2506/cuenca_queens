##N Queens in Python

##Instructions to follow
**Will need for you to have Docker & Docker Compose**
1. Clone repo: `git clone https://github.com/marcocastillo2506/cuenca_queens.git`
2. Build containers: `docker-compose up --build -d`
3. Execute main program: `docker-compose run queens`

######*Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle*

These are the different aspect of the project you can work on (in order):<br>
1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens<br>
2. iterate over N and store the solutions in postgres using SQLAlchemy<br>
3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest<br>
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)<br>
5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically<p>
