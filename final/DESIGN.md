This website was heavily implemented using Python, SQL, Javascript, HTML, and CSS.

The register/log in page were implemented using HTML, CSS, Python, and SQL in order to log in and record that all users have the same password and confirmation password. Once registered,
the users are able to log in using their respective information. Once logged in, the user will be shown the home page.

The home page heavily relied on HTML, CSS, and Bootstrap. Upon seeing the home page, users will notice that there is a carousel slider of images all dealing with the pandemic.
This was done with several boostrap classes including but not limited to carousel-item, container fluid, etc. The bootstrap documentation is cited as well as the font awesome
icons I used such as the mask symbol, the hospital symbol, and the medical kit symbol. I implemented a footer and a navigation header using HTML and CSS.

In addition to the home page, the about section of the website was also implemented using HTML, CSS, and Bootstrap. I used an heading element, as well as several
paragraph elements to display some general and specific information about COVID Times. In addition, I included an image of a mask and stylized it with CSS. For example, I
experimented with the box-shadow, which implemented a shadow around the image, and border-radius, which ultimately made the border around the image circular.

Next, I implemented the News part of the website. This was much more difficult as it involved using an API, which I had no previous experience with. However, with enough research and
documentation (sources cited as comments as well as the documentation that helped me get a clear idea on how to use this API) I was able to succesfully implement it. Essentially, the news
page of the website uses HTML, CSS, and Javascript to fetch all of the information from the New York Times API. The javascript part of this implmentation can be found in the file
"news.html" near the bottom surrounded by script tags. I used a URL that filtered the articles to the topic of health and this was acquired from the New York Times API, which I had to create
an account for. In order to use the New York Times API, I fetched the data from the url using fetch(url) and also using the API key assigned to me, and had to parse in terms of JSON and I had to convert it to a normal Javascript
object that I could manipulate and experiment with. I then had to use the array full of javascript objects. I only wanted the title of the article, a short description, and the corresponding
image to display. In order to access all of the data, I had to use the map function to go over everything in the array. This allowed me to go through the array and extract the title, description, and image.
I then had to create the a element in javascript using the .createElement function. In order to link to that a tag, I used the .setAttribute
that would take the user to the url for that article.


Lastly, I then had to use the appendChild method to add to my headlines div every image, description, and article title from the API. All of the articles and
documentation that I used for help and guidance are cited inside comments above the script tag.

I made the decision to only display the image, article, and a short description for each article in order to provide a concise list of articles for the user. I wanted the users to
get a quick idea and brief summary of the articles they were searching for.

The last page of the website is called "Resources" and this was implemented using HTML and CSS. This page provides links to helpful resources and it was stylized with CSS.

