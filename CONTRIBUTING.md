# Contributing to Developers India Resources

First off, thanks for taking the time to contribute! 🎉
Make sure you follow below guidelines before contributing.

## What qualifies as a "resource"?

- Anything which can be used/referenced to learn something. We only accept following types of resources:
  1. Book
  2. Video
  3. Article
  4. Cheatsheet
  5. Online Course (Free/Paid)
  6. Github Repository
  7. Audio (any podcasts)
  8. Website (Anything dedicated to learning one thing. For ex. `javascript.info` qualifies as a "Website" resource for "JavaScript" whereas `colorlib.com` doesn't qualify as a resource for "CSS".


## How to add a new resource?

1. Figure out the correct directory for your resource, E.g. If you are adding a "Python" resource, you will have to edit the `index.json` file in `languages/python` directory.
   > If no appropriate directory exists for your resource, add it inside `miscellaneous/index.json`.

2. Go to the bottom of the json file and add a object like this.
   ```json
   {
       "title":"",
       "url":"",
       "type":"",
       "level":"",
       "reviews": []
   }
   ```

   Reference the below table for description of each JSON key.

   |    Key    |                                                                          Description                                                                         |
   |:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
   |  `title`  | The title of resource. If you are contributing a book resource you can choose to mention the author                                                          |
   |   `url`   | The permalink to the resource. No links that redirect anywhere.                                                                                              |
   |   `type`  | What type of resource is this:<br>1. `book`<br>2. `video`<br>3. `article`<br>4. `cheatsheet`<br>5. `course`<br>6. `github`<br>7. `audio`<br>8. `website`<br> |
   |  `level`  | What is the best audience for consuming this resource<br>1. `beginner`<br>2. `intermediate`<br>3. `advanced`<br>4. `everyone`                                |
   | `reviews` | Add you review of this resource.<br>- What did you learn from it?<br>- What was special or interesting about it?<br>- Why do you recommend this resource?                   |

   This is how a correct object looks like:

   ```json
   {
       "title":"learnopengl.com",
       "url":"https://learnopengl.com/",
       "type":"book",
       "level":"everyone",
       "reviews":[
           "You should only follow concepts here, not api"
       ]
   }
   ```
   > We highly encourage contributors to add their review to provide a community aspect for the resource. If you have nothing to say about the resource you can omit adding the "reviews" key.

3. Make you changes to `feature` branch & send a PR (See if there is already an open PR with the same contribution).
4. Feel free to ask doubts, just open an [issue](https://github.com/developersIndia/resources/issues/new).
