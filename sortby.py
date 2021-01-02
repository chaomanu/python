# a template for a databank
# takes data as input and can be sorted by each of the categories
# choose between a certain value for a category or choose between 1 and 10 for 10 as the max value
# use sql to determine primary value - numbered
# make an app for tcm foods

primaryval = [0,1,2,3]
food = ["zucchini", "raspberry", "chicken meat"]

categories = ["vegetable", "fruit", "meat"]
tastes = ["sweet", "sour", "pungent", "bitter", "salty", "tasteless", "astringent"]
thermaldict = {1: "very cold", 2: "cold", 3: "cool", 4: "slightly cool", 5: "neutral", 6: "slightly warm", 7: "warm", 8: "hot", 9: "very hot"}

print(food[1]+ ": " + categories[1] + ", taste is " + tastes[1] + ", thermal property is " + thermaldict[3])