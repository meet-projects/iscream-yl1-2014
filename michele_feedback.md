Michele's group project feedback
---

Thank you for getting the project to me, even though it was difficult for you. I have a few comments about your project: 

* Your `clear_screen` function and your `Label`, `button`, and `picture` classes are great.
* Your `button` and `Label` classes are similar - you could have made `Label` a subclass of `button`, to save some code to re-write
* I really like what you did with the `welcomscreen` file. You created a page inside a function on the `welcomscreen.py` file, then imported that file into the `main.py` file, and ran that function from your `if __name__=="__main__"`. It is a great way of splitting up work between group members, if they are working on different files and pieces of the program. Your group should do this for the other pages in your program - this was already started, but the problem was that the integration did not happen in the `main.py` file, but all the code was copied over (or re-written). It is much easier to import the file and call the function than re-write all the code. 
* Good job using the `stepNum` and `scoopnum` variables to keep track of what screen the user was looking at.
* At one point in your `while` loop, you are using two different variables, both called `x`. In this case you got lucky because they did not interfere with each other, but in other cases this might be a serious problem. 
* I would have loved to see a `back` button in your program in case I want to order a new ice cream, or if I mess up. It should be fairly easy to add, since your logic is good. 
* It would also have been nice to have the "x" on the corner of the pygame window close the program. There is example code on the student website in the example code I gave. 