learner = "James"
questions = 24
correct = 19

points_per_correct = 4
penalty_per_incorrect = 2
bonus_points = 5

minimum_accuracy = 75
minimum_score = 50

# Requirements
# 1. Calculate the number of incorrect answers, the total points earned from correct answers, the total penalties, 
# the final score (earned points minus penalties plus bonus), and the accuracy percentage.

# 2. Then create two Boolean variables: accuracy_requirement_met and score_requirement_met. Finally, create qualified 
# using logical and so that it is True only when both requirements are met.

# 3. Display a readable summary containing the learner's name, correct and incorrect answers, final score, accuracy 
# (one decimal place), and qualification status.

incorrect = questions - correct
points_earned = correct * points_per_correct
total_penalties = incorrect * penalty_per_incorrect
final_score = points_earned - total_penalties + bonus_points
accuracy = correct/questions*100

accuracy_requirement_met = accuracy >= minimum_accuracy
score_requirement_met = final_score >= minimum_score

qualified = accuracy_requirement_met and score_requirement_met

print(f"Learner: {learner}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Final score: {final_score}")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Qualification status: {qualified}")