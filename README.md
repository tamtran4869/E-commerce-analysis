# E-commerce-analysis

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">An E-commerce Analysis And Visualisation Project</h3>

  <p align="center">
    The project is guided by Maven Analytics through the course the advanced SQL in Udemy.
    <br />
     However, there are some tasks after extracting required data, it is hard to get ideas, insights or conclusions from dataframs. Therefore, to make it clear and practice more skills, besides SQL as the course, I used SQL and Python for extract data and create visualization with mabplotlib, plotly, seaborn; and Tableau for building final dashboards.
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- CONTEXT -->
## About the course

[![Product Name Screen Shot][product-screenshot]](https://example.com)
The purpose of the Udemy course is to deal with real-life, ad-hoc requirements of stakeholders to extract and analyse data from database of the Maven Fuzzy Factory - a new online retailer. 
The course included a serires of ad-hoc tasks from marketing and website management teams and full reports task from the CEO.

You can find the detail <a href="https://www.udemy.com/course/advanced-sql-mysql-for-analytics-business-intelligence/">here.</a>
I highly recommend the course for getting more advance in SQL.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About Maven Fuzzy Factory

[![Product Name Screen Shot][product-screenshot]](https://example.com)
It is an ecommerce company selling stuffies. See some events of the company during 3 years (Mar 2012 - Mar 2015) below:

- Mar 2012: Launched the first product (Mr.Fuzzy).
- Nov 2012: First reviewed the whole business growth after 8 months launching
- Jan 2013: Launched another new product (Love Bear).
- Sep 2013: Offered the option to add 2 products into cart.
- Dec 2013: Launched another new product (Birthday bear).
- Sep 2014: Fixed the problem with bears's arm.
- Mar 2015: Second reviews after 3 years in market.

During 3 years, the team was continuously analysied data to optimise marketing channels, platforms and website; understand insight users with product, behavior in website and refund data to make decisions.  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About the project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
This is the schema of mavenfuzzyfactory database.
 ![image](https://user-images.githubusercontent.com/114192113/211662502-b3a93ec0-a920-4e5b-b777-10a234cef385.png)

Generally, there are 6 main analysis directions related to the e-commerce business:

- Traffic source analysis to evaluate different marketing channel performance.
- Website performance analysis to assess the website structure.
- Time series analysis to discover the correlation between time vs traffic.
- Product analysis to know more about the situation of the new launched product.
- User analysis to get users insight and behavior on the website.
- Business growth analysis to get picture about the business "health".

This project covers 21 questions and 1 final dashboard which included 6 main directions to make a story about the growth of Maven Fuzzy Factory. (You can find more tasks in the Udemy course)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Upload the mavenfuzzyfactory database into the SQL server by <a href="https://github.com/othneildrew/Best-README-Template"> the SQL file</a>.

Running query in Python through SQL connections is more convenient for questions needed visualisation. Therefore, the project included a small Python code to follow questions more easy and consistent.

SQL query of each question are stored into 2 txt of files in question folder: txt (for running without comment) and sql (for reading with comment and can used directly in SQL). 


### Installation
Clone the repo and go to the project folder
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   cd ecommerce_analysis
   ```
 ### Usage
Use the connect.py file to run or read the query of each question by the command.

The db parameter has structure 'database_name user password'.
   ```sh
   python3 --question 8 --db 'mavenfuzzyfactory user password' --task 'run' #or 'read'

   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
The detailed tasks
### Traffic source analysis

The benefit is assess performance of each channels-platforms to adjust the bidding, decide to stop the channels.

- <a href="https://github.com/othneildrew/Best-README-Template">Question 0 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 1 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 2 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 3 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 4 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 5 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 6 </a>

### Website performance analysis

This analysis is to optimize, do A/B testing with landing page; check bounding rates , check conversion funnel to check whether the significant drop in each goals.

- <a href="https://github.com/othneildrew/Best-README-Template">Question 7 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 8 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 9 </a>

### Time series analysis

By looking at this type of analysis, the business could understand correlations between time (moth, week, day, hours) and metrics (example in this case is the website session).

- <a href="https://github.com/othneildrew/Best-README-Template">Question 10 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 11 </a>

### Product analysis
The product analysis helps find the the problem with product with refund data, evaluate new product launching, compare products (funnel) and cross-sell.

- <a href="https://github.com/othneildrew/Best-README-Template">Question 12 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 13 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 14 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 15 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 16 </a>



### User analysis
To get more data about user bahavior (e.g. return, spending time, purchase) in the website, the user analysis need to be investigated.

- <a href="https://github.com/othneildrew/Best-README-Template">Question 17 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 18 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 19 </a>
- <a href="https://github.com/othneildrew/Best-README-Template">Question 20 </a>

### Business growth

Beside ad-hoc tasks, the final report/dashboard bring the compete view for the team about the business state. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
