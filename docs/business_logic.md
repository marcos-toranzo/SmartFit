# Business Logic

The database for the app will be initially populated with basic routines for general workout sessions, elaborated with the collaboration of specialists on the topic. With this basic information, the system will be able to recommend routines, as well as start calculating optimal workouts based on the information provided by the user (like what kind of exercise has been done or which specific areas of the body to avoid exercise) and what are the properties of the stored routines and how they match with the required workout, using machine learning and data processing algorithms.

## The **User** entity contains:

- Personal information (name, etc.)
- Physical fitness information (age, general health, height, weight, physical activity, etc.). This information will be used in some predictions for getting the best recommendations.
- Rating (how good of a contributor is the user, how good are the routines submitted by the user, etc.). This information will also be used for the recommendation and optimization systems when selecting the best routines.

## The **Exercise** entity contains:

- A simple description.
- A series of steps to follow (pictures, videos, etc).
- A workout load table.

## The **Routine** entity contains:

- A simple description.
- The user that uploaded it.
- The likes or upvotes that it has (the bigger, the better).
- Comments and feedback from users.
- Keywords and tags indicating instructions or why would you do this routine.
- A series of exercises that comprehend the actual routine.
- A total workout load table based on the individual workout from the exercises.

Users, as contributors, will be able to upload or submit their own routines with specific tags like: `avoid legs`, `for neck stiffness` and `after a long walk`. They can choose to make them public (for others to use and rate), or private, where only they can access them, like saving it for another day. This way the systems hability to recommend and optimize routines improves, learning from real life experiences from active users.

Also, users acting as consumers will be able to consult for specific routines depending on the day they had, maybe by entering the areas of the bodies they want to avoid (prioritize), or by explaining the type of work they have done so far and the system would identify the affected areas automatically, in case of being possible. This, together with the general information of the user, the tracked information (previous experiences, likes and dislikes and weekly schedule) and the history, will provide enough information for the system to make a good recomendation of which routine to do, and how or when to do it.

The workout load will consist of some kind of table indicating the stress that the exercise puts on the specific parts of the body, ranging from 0 (none) to 100 (full workload). For example, for simple squatting, the table could be: `Quadriceps -> 80`, `Calfs -> 70`, `Abdomen -> 10`. This values will be analyzed to compute the table for the whole routine, using some wighted average algoritm or something more complex. With this table, the system will be able to calculate an optimal solution for a specific workout based on the table that the user enters specifying what parts of the body have been affected during the day, and which ones he/she wants to exercise.

For example, if the user enters:

- **Avoid**: Abdomen -> 60, Legs -> 50;

- **Exercise**: Biceps -> 60, Back -> 50;

then the system will work on a solution to achieve these values, minimizing the strain on the abdomen and legs (allowing a little more legs than abdomen) while maximizing the workload on the biceps and back (exercising a little more the biceps than the back).
