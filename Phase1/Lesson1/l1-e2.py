learner = "Anna"
total_questions = 20
correct_answers = 17
study_minutes = 45

# Learner: Anna
# Correct: 17
# Incorrect: 3
# Accuracy: 85.0%
# Average time: 135.0 seconds
# Passed: True

accuracy = correct_answers/total_questions*100
passed = accuracy >= 80

print(f"Learner: {learner}")
print(f"Correct: {correct_answers}")
print(f"Incorrect: {total_questions - correct_answers}")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Average time: {((study_minutes/total_questions)*60):.1f} seconds")
print(f"Passed: {passed}")