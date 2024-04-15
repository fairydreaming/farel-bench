#!/usr/bin/env python3

import codecs
import random
import sys

DEFAULT_PROMPT = "Given the family relationships:\n$QUIZ_RELATIONS\n$QUIZ_QUESTION\nSelect the correct answer:\n$QUIZ_ANSWERS\nEnclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>."

male_names = [
    'James', 'Robert', 'John', 'Michael', 'David',
    'William', 'Richard', 'Joseph', 'Thomas', 'Christopher',
    'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark',
    'Donald', 'Steven', 'Andrew', 'Paul', 'Joshua',
    'Kenneth', 'Kevin', 'Brian', 'George', 'Timothy',
    'Ronald', 'Jason', 'Edward', 'Jeffrey', 'Ryan',
    'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan',
    'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon',
    'Benjamin', 'Samuel', 'Gregory', 'Alexander', 'Patrick',
    'Frank', 'Raymond', 'Jack', 'Dennis', 'Jerry',
    'Tyler', 'Aaron', 'Jose', 'Adam', 'Nathan',
    'Henry', 'Zachary', 'Douglas', 'Peter', 'Kyle',
    'Noah', 'Ethan', 'Jeremy', 'Walter', 'Christian',
    'Keith', 'Roger', 'Terry', 'Austin', 'Sean',
    'Gerald', 'Carl', 'Harold', 'Dylan', 'Arthur',
    'Lawrence', 'Jordan', 'Jesse', 'Bryan', 'Billy',
    'Bruce', 'Gabriel', 'Joe', 'Logan', 'Alan',
    'Juan', 'Albert', 'Willie', 'Elijah', 'Wayne',
    'Randy', 'Vincent', 'Mason', 'Roy', 'Ralph',
    'Bobby', 'Russell', 'Bradley', 'Philip', 'Eugene'
]

female_names = [
    'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth',
    'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
    'Lisa', 'Nancy', 'Betty', 'Sandra', 'Margaret',
    'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle',
    'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie',
    'Dorothy', 'Rebecca', 'Sharon', 'Laura', 'Cynthia',
    'Amy', 'Kathleen', 'Angela', 'Shirley', 'Brenda',
    'Emma', 'Anna', 'Pamela', 'Nicole', 'Samantha',
    'Katherine', 'Christine', 'Helen', 'Debra', 'Rachel',
    'Carolyn', 'Janet', 'Maria', 'Catherine', 'Heather',
    'Diane', 'Olivia', 'Julie', 'Joyce', 'Victoria',
    'Ruth', 'Virginia', 'Lauren', 'Kelly', 'Christina',
    'Joan', 'Evelyn', 'Judith', 'Andrea', 'Hannah',
    'Megan', 'Cheryl', 'Jacqueline', 'Martha', 'Madison',
    'Teresa', 'Gloria', 'Sara', 'Janice', 'Ann',
    'Kathryn', 'Abigail', 'Sophia', 'Frances', 'Jean',
    'Alice', 'Judy', 'Isabella', 'Julia', 'Grace',
    'Amber', 'Denise', 'Danielle', 'Marilyn', 'Beverly',
    'Charlotte', 'Natalie', 'Theresa', 'Diana', 'Brittany',
    'Doris', 'Kayla', 'Alexis', 'Lori', 'Marie'
]

class FamilyRelationTemplate:
    def __init__(self, parental_relations, question_characters, genders = []):
        self.parental_relations = parental_relations
        self.relation_characters = question_characters
        self.genders = genders
    def __repr__(self):
        return str(self.parental_relations) + ", " + str(self.relation_characters) + ", " + str(self.genders)

def generate_nth(level):
    if level == 0:
        return ""
    elif level == 1:
        return "1st "
    elif level == 2:
        return "2nd "
    elif level == 3:
        return "3rd "
    else:
        return str(level) + "th "

def generate_grand(level, relation):
    if level == 0:
        return relation
    separator = ''
    if relation in ["aunt", "uncle", "niece", "nephew"]:
        separator = '-'
    if level < 4:
        return "great " * (level - 1) + "grand" + separator + relation
    else:
        return generate_nth(level - 1) + "great grand" + separator + relation

def generate_x(level):
    if level == 0:
        return ""
    else:
        return " " + str(level) + "x removed"

def generate_relation_name(row, level):
#    print(row, level)
    if row == 0:
        return generate_grand(level - 1, "child")
    elif row == 1:
        if level == 0:
            return "sibling"
        elif level > 0:
            return generate_grand(level - 1, "niece") + " or " + generate_grand(level - 1, "nephew")
        else:
            assert(False)
    else:
        if level == -row:
            return generate_grand(row - 1, "parent")
        elif level == -row + 1:
            return generate_grand(row - 2, "aunt") + " or "  + generate_grand(row - 2, "uncle")
        elif level < 0:
            return generate_nth(row + level - 1) + "cousin" + generate_x(-level)
        else:
            return generate_nth(row - 1) + "cousin" + generate_x(level)
    return ""

def grow_relation_trees(nth_level_trees, nth_level_names, nth_level_indexes, nth_level_levels):
    # create a new branch of family tree by adding another ancestor
    current_index = nth_level_indexes[-1]
    current_level = nth_level_levels[-1]
    new_branch_tree = nth_level_trees[-1].copy()
    new_branch_tree.append((current_index + 1, current_index))
    nth_level_names.append(generate_relation_name(-current_level + 1, current_level - 1))
    nth_level_indexes.append(current_index + 1)
    nth_level_levels.append(current_level - 1)

    # for each tree in a list add a new leaf
    for row, relation_tree in enumerate(nth_level_trees):
        current_index = nth_level_indexes[row]
        current_level = nth_level_levels[row]
        nth_level_trees[row].append((current_index, current_index + 1))
        nth_level_names[row] = generate_relation_name(row, current_level + 1)
        nth_level_indexes[row] = current_index + 1
        nth_level_levels[row] = current_level + 1

    # finally append a new tree to the list
    nth_level_trees.append(new_branch_tree)
#    print(nth_level_trees, nth_level_names, nth_level_indexes, nth_level_levels)

def generate_relation_paths(to_level):
    nth_level_names = ["child", "parent"]
    nth_level_indexes = [1, 1]
    nth_level_levels = [1, -1]
    nth_level_trees = [[(0, 1)], [(1, 0)]]

    for i in range(len(nth_level_trees)):
        yield nth_level_names[i], nth_level_trees[i], (nth_level_indexes[i], 0)
            
    for level in range(1, to_level):
        grow_relation_trees(nth_level_trees, nth_level_names, nth_level_indexes, nth_level_levels)
        for i in range(len(nth_level_trees)):
            yield nth_level_names[i], nth_level_trees[i], (nth_level_indexes[i], 0)

def grow_family_tree(nth_level_tree, nth_level_names, nth_level_indexes, next_index, nth_level_levels):
    # create a new branch of family tree by adding another ancestor
    parent_index = nth_level_indexes[-1]
    parent_level = nth_level_levels[-1]

    # for each tree in a list add a new leaf
    for row in range(len(nth_level_indexes)):
        current_index = nth_level_indexes[row]
        current_level = nth_level_levels[row]
        nth_level_tree.append((current_index, next_index))
        nth_level_names[row] = generate_relation_name(row, current_level + 1)
        nth_level_indexes[row] = next_index
        nth_level_levels[row] = current_level + 1
        next_index += 1

    nth_level_tree.append((next_index, parent_index))
    nth_level_names.append(generate_relation_name(-parent_level + 1, parent_level - 1))
    nth_level_indexes.append(next_index)
    nth_level_levels.append(parent_level - 1)
    next_index += 1
#    print(nth_level_tree, nth_level_names, nth_level_indexes, nth_level_levels)

    return next_index

def generate_relation_trees(to_level):
    nth_level_names = ["child", "parent"]
    nth_level_indexes = [1, 2]
    nth_level_levels = [1, -1]
    nth_level_tree = [(0, 1), (2, 0)]
    next_index = 3

    yield 1, nth_level_tree, nth_level_names, nth_level_indexes
    
    for current_level in range(2, to_level + 1):
        next_index = grow_family_tree(nth_level_tree, nth_level_names, nth_level_indexes, next_index, nth_level_levels)
        yield current_level, nth_level_tree, nth_level_names, nth_level_indexes


def assign_character_name(gender, male_names_iter, female_names_iter):
    if gender == "male":
        return next(male_names_iter)
    elif gender == "female":
        return next(female_names_iter)
    else:
        assert(False)

def generate_quiz(relation_template, relation_names, relations_to_generate=None, shuffle=False, prompt=DEFAULT_PROMPT):
    num_template_relations = len(relation_template.parental_relations)

    # if number of generated relations is not specified, generate only the relations from template
    if relations_to_generate is None:
        relations_to_generate = num_template_relations

    assert(relations_to_generate >= num_template_relations)

    quiz_relations = relation_template.parental_relations.copy()
    
    num_template_characters = len({ p for rel_tuple in relation_template.parental_relations for p in rel_tuple })
    num_quiz_characters = num_template_characters + 2 * (relations_to_generate - num_template_relations)

    # generate additional random relations if needed
    non_template_characters_iter = iter(range(num_template_characters, num_quiz_characters + 1))
    for i in range(relations_to_generate - num_template_relations):
        quiz_relations.append((next(non_template_characters_iter), next(non_template_characters_iter)))

    if shuffle:
        random.shuffle(quiz_relations)

    # randomly generate genders of the quiz characters
    gender_list = ['male', 'female']
    character_genders = [random.choice(gender_list) for _ in range(num_quiz_characters)]
    
    # overwrite genders for characters specified in relation template
    for (character_index, character_gender) in relation_template.genders:
        character_genders[character_index] = character_gender

    # assign names to the quiz characters based on their genders
    male_names_iter = iter(random.sample(male_names, len(male_names)))
    female_names_iter = iter(random.sample(female_names, len(female_names)))
    character_names = [assign_character_name(character_genders[c], male_names_iter, female_names_iter) for c in range(num_quiz_characters)]
    
    quiz_relations_str = ""
    for p1, p2 in quiz_relations:
        p1_name = character_names[p1]
        p2_name = character_names[p2]
        s = "" if p2_name.endswith("s") else "s"
        quiz_relations_str += f"* {p1_name} is {p2_name}'{s} parent.\n"

    p1, p2 = relation_template.relation_characters
    p1_name = character_names[p1]
    p1_name_s = p1_name + "'" + ("" if p1_name.endswith("s") else "s")
    p2_name = character_names[p2]
    p2_name_s = p2_name + "'" + ("" if p2_name.endswith("s") else "s")

    quiz_genders_str = ""
    for (character_index, character_gender) in relation_template.genders:
        p_name = character_names[character_index]
        quiz_genders_str += f"{p_name} is {character_gender}. "
    
    quiz_question_str = f"What is {p1_name_s} relationship to {p2_name}?"
    quiz_answers_str = f""
    for i, name in enumerate(relation_names):
        answer_num_str = str(i+1) + "."
        quiz_answers_str += f"{answer_num_str} {p1_name} is {p2_name_s} {relation_names[i]}.\n"

    quiz = prompt
    quiz = quiz.replace("$QUIZ_RELATIONS", quiz_relations_str.strip())
    quiz = quiz.replace("$QUIZ_GENDERS", quiz_genders_str.strip())
    quiz = quiz.replace("$QUIZ_QUESTION", quiz_question_str.strip())
    quiz = quiz.replace("$QUIZ_ANSWERS", quiz_answers_str.strip())
    return quiz

def generate_quizzes(max_length, num_quizzes=10, prompt=DEFAULT_PROMPT, shuffle=False, seed=None):
    if seed is not None:
        random.seed(seed)
    for (level, tree, names, indexes) in generate_relation_trees(max_length):
        print(f"Relations of length: {level} ({names})", file=sys.stderr)
        for i, relation_name in enumerate(names):
            relation_template = FamilyRelationTemplate(tree, (indexes[i], 0))
            for j in range(num_quizzes):
                answer_options = random.sample(names, len(names)) if shuffle else names
                correct_answer = str(answer_options.index(relation_name)+1)

                quiz = generate_quiz(relation_template, answer_options, shuffle=shuffle, prompt=prompt)
                yield (level, relation_name, correct_answer , quiz)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help = "Maximum length of family relationship paths.", type=int, required=True)
    parser.add_argument("-p", "--prompt", help = "Prompt template of the quiz. The default prompt template is: " + repr(DEFAULT_PROMPT), default=DEFAULT_PROMPT)
    parser.add_argument("-s", "--shuffle", help = "Shuffle the order of parental relations and answer options in the quiz.", action="store_true")
    parser.add_argument("-n", "--number", help = "Number of quizzes generated for each family relationship.", default=10, type=int)
    parser.add_argument("-r", "--seed", help = "Random seed value", default=None, type=int)
    args = parser.parse_args()

    prompt = codecs.escape_decode(bytes(args.prompt, "utf-8"))[0].decode("utf-8")

    for level, relation_name, correct_answer, quiz in generate_quizzes(args.length, args.number, prompt, args.shuffle, args.seed):
        print(f"{level},{relation_name},{correct_answer},{repr(quiz)}")
 
