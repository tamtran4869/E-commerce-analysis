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
    The project is guided by Maven Analytics with the advanced SQL course in Udemy.
    
However, after extracting the required data, there are some tasks; getting ideas, insights or conclusions from data frames is hard. Therefore, to make it clear and practice more skills, besides SQL as the course, I used Python to extract data and create visuals and commented insights getting from it.
   
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

The purpose of the Udemy course is to deal with real-life, ad-hoc requirements of stakeholders to extract and analyse data from the Maven Fuzzy Factory database - a new online retailer. The course included a series of ad-hoc tasks from marketing and website management teams and full reports tasks from the CEO.

You can find the detail <a href="https://www.udemy.com/course/advanced-sql-mysql-for-analytics-business-intelligence/">here.</a>
I highly recommend the course for getting more advance in SQL.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About Maven Fuzzy Factory

[![Product Name Screen Shot][product-screenshot]](https://example.com)

It is an e-commerce company selling stuffies. See some events of the company during three years (Mar 2012 - Mar 2015) below:

- Mar 2012: Launched the first product (Mr Fuzzy).
- Nov 2012: First reviewed the whole business growth after eight months of launching
- Jan 2013: Launched another new product (Love Bear).
- Sep 2013: Offered the option to add two products to the cart.
- Dec 2013: Launched another new product (Birthday bear).
- Sep 2014: Fixed the problem with the bear's arm.
- Mar 2015: Second review after three years in the market.

During three years, the team continuously analysed data to optimise marketing channels, platforms and websites, understand insight users with products, and behaviour on the website and refund data to make decisions. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About the project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
This is the schema of mavenfuzzyfactory database.
 ![image](https://user-images.githubusercontent.com/114192113/211662502-b3a93ec0-a920-4e5b-b777-10a234cef385.png)

Generally, there are six main analysis directions related to the e-commerce business:

- Traffic source analysis to evaluate different marketing channel performance.
- Website performance analysis to assess the website structure.
- Time series analysis to discover the correlation between time and traffic.
- Product analysis to know more about the situation of the newly launched product.
- User analysis to get users' insight and behaviour on the website.

This project covers 21 questions and one final dashboard, which includes these main directions to make a story about the growth of Maven Fuzzy Factory. (You can find more tasks in the Udemy course).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Upload the mavenfuzzyfactory database into the SQL server by <a href="https://github.com/othneildrew/Best-README-Template"> the SQL file</a>.

Running queries in Python through SQL connections is more convenient for questions needing visualisation. Therefore, the project included a small Python code to follow questions more easily and consistently.

SQL queries of each question were stored in a txt file (for running without comment).

### Installation
Clone the repo and go to the project directory.
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   cd ecommerce_analysis
   ```
 ### Usage
Use the connect.py file to run the query of each question by the command.

The db parameter has structure 'database_name user password'.
   ```sh
   python3 --question 8 --db 'mavenfuzzyfactory user password'

   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

This work covered SQL for getting data (not maintain the database) with complex using SELECT, COUNT, DISTINCT, CASE WHEN, JOIN, multiple window functions, subqueries. View SQL queries in the <a href="https://github.com/othneildrew/Best-README-Template"> question </a>  folder.

Besides, various type of charts were used to fit with the data from simple (e.g. pie, line, bar) to complex (e.g. heatmap, funnel, combined charts). View the python code for visualisation in <a href="https://github.com/othneildrew/Best-README-Template"> get_df_visual.py </a> file and the charts in the <a href="https://github.com/othneildrew/Best-README-Template"> fig </a> folder.

### Traffic source analysis

The benefit is to assess the performance of each channels, platforms to adjust the bidding, decide to focus on which channels, which platforms and define the targeting (e.g. device type)

<a href="https://github.com/othneildrew/Best-README-Template">Go to the section > </a>

### Website performance analysis

This analysis is to optimize, do A/B testing with the landing page, check bounce rates, and examine the conversion funnel to check whether the a significant drop in each goal.

<a href="https://github.com/othneildrew/Best-README-Template">Go to the section > </a>

### Time series analysis

By looking at this type of analysis, the business could understand correlations between time (month, week, day, hours) and metrics (e.g. in this case, the website session) that help the marketing team to set up ads, the operation team to prepare stocks and staffs, plan sale and events; the website team to make the website accessible even with massive traffic. 

<a href="https://github.com/othneildrew/Best-README-Template">Go to the section > </a>

### Product analysis
The product analysis helps find the problem with the product with refund data, evaluate new product launching, compare products (the funnel) and cross-sell.

<a href="https://github.com/othneildrew/Best-README-Template">Go to the section > </a>



### User analysis
The user analysis needs to be investigated to understand user behaviour (e.g. return, spending time, purchase) to plan a custom strategy for each segment. The word 'user' means different in different scenarios. It could be consumers with purchasing data, audiences (in advertising) with behaviour and insights data (e.g. click, share, interests), users with session data on the website, students with information and results data, etc.


In this work, it analysed users' behaviour on the websites.

<a href="https://github.com/othneildrew/Best-README-Template">Go to the section > </a>






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
